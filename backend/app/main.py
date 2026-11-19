
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import fitz
from app.gemini_service import ask_gemini
from pydantic import BaseModel
# Create the FastAPI application
app = FastAPI(
    title="BungeLens API",
    description="AI-powered Kenyan civic education platform",
    version="1.0.0"
)

# Allow our frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


@app.get("/")
def home():
    return {
        "message": "Welcome to BungeLens API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "BungeLens"
    }


@app.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):

    # Check that the uploaded file is a PDF
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF documents are accepted."
        )

    contents = await file.read()

    # Check file size
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File exceeds the 10 MB limit."
        )

    # Check that the file has a PDF signature
    if not contents.startswith(b"%PDF-"):
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is not a valid PDF."
        )

    try:
        document = fitz.open(
            stream=contents,
            filetype="pdf"
        )

        extracted_pages = []

        # Extract text page by page
        for page_number, page in enumerate(document, start=1):
            page_text = page.get_text("text")

            extracted_pages.append({
                "page": page_number,
                "text": page_text
            })

        total_pages = len(document)
        document.close()

        full_text = "\n".join(
            page["text"] for page in extracted_pages
        )

        if not full_text.strip():
            raise HTTPException(
                status_code=422,
                detail="No readable text found. This may be a scanned PDF."
            )

        return {
            "message": "Document uploaded and processed successfully",
            "filename": file.filename,
            "total_pages": total_pages,
            "extracted_text": full_text,
            "pages": extracted_pages
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to process this PDF document."
        )

class DocumentQuestion(BaseModel):
    document_text: str
    question: str


@app.post("/documents/ask")
async def ask_document(request: DocumentQuestion):

    if not request.document_text.strip():
        raise HTTPException(
            status_code=400,
            detail="Document text cannot be empty."
        )

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Please enter a question."
        )

    prompt = f"""
    You are BungeLens, an AI assistant specializing
    in explaining Kenyan civic and legal documents.

    Answer the user's question using ONLY the supplied
    document.

    If the answer is not in the document, say so clearly.
    Do not invent laws, clauses or legal references.

    Explain complicated legal language in simple English.
    Include relevant page or clause references when available.

    DOCUMENT:
    {request.document_text}

    USER QUESTION:
    {request.question}
    """

    try:
        answer = ask_gemini(prompt)

        return {
            "status": "success",
            "question": request.question,
            "answer": answer
        }
    except Exception as e:
        print(f"GEMINI ERROR: {repr(e)}")

        raise HTTPException(
            status_code=502,
            detail="Unable to get a response from Gemini."
        )

