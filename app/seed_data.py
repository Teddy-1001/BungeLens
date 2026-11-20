from typing import Any

from app.database import seed_record_if_missing


LESSONS: list[dict[str, Any]] = [
    {
        "id": "constitution-rights",
        "topic": "Constitution",
        "title": "How the Constitution protects your rights",
        "description": "Start with fundamental rights and where to find them in the Constitution.",
        "level": "Beginner",
        "duration": "5 min",
        "icon": "shield",
        "introduction": "The Constitution sets out rights and freedoms, explains who has duties to protect them, and provides ways to seek help when rights are limited or violated.",
        "sections": [
            {
                "heading": "Start with the relevant article",
                "body": "Find the article that describes the right you want to understand. Read the surrounding clauses too, since they may explain limits, responsibilities or how the right works.",
            },
            {
                "heading": "Connect the text to daily life",
                "body": "Ask what the right means in practice, who has a responsibility to respect it, and what public service or decision may be involved.",
            },
            {
                "heading": "Check the source",
                "body": "Use the official Constitution text to confirm the article wording. Treat plain-language notes as a guide to learning, not as a replacement for the original text.",
            },
        ],
        "takeaways": [
            "Use the article number when looking up a constitutional right.",
            "Read related clauses before drawing conclusions.",
            "Check the original text and seek qualified help for a specific legal problem.",
        ],
        "sourceUrl": "https://new.kenyalaw.org/akn/ke/act/2010/constitution",
        "sourceName": "Kenya Law",
        "next": "bill-process",
    },
    {
        "id": "bill-process",
        "topic": "Parliament",
        "title": "How a bill becomes law",
        "description": "Follow the main steps a proposal takes through Parliament.",
        "level": "Beginner",
        "duration": "6 min",
        "icon": "file",
        "introduction": "A bill is a proposal for a new law or a change to existing law. Its route through Parliament can involve several readings, committee consideration and other required steps.",
        "sections": [
            {
                "heading": "Find the bill and its sponsor",
                "body": "Start with the official bill text and record its bill number, sponsoring member or ministry, and the House considering it.",
            },
            {
                "heading": "Follow the stages",
                "body": "Track the bill’s official progress. The steps can differ depending on the bill and the constitutional process that applies, so verify each update against parliamentary records.",
            },
            {
                "heading": "Look for opportunities to participate",
                "body": "Parliament or a committee may invite public views. Check official notices for deadlines, submission instructions and the committee’s contact details.",
            },
        ],
        "takeaways": [
            "A bill is a proposal; it is not automatically law.",
            "Use the bill number to distinguish it from other proposals.",
            "Verify the latest stage and participation notices from official sources.",
        ],
        "sourceUrl": "https://www.parliament.go.ke/the-national-assembly/house-business/bills",
        "sourceName": "Parliament of Kenya",
        "next": "committees",
    },
    {
        "id": "committees",
        "topic": "Parliament",
        "title": "What parliamentary committees do",
        "description": "Learn how committees examine issues and may gather public input.",
        "level": "Beginner",
        "duration": "4 min",
        "icon": "search",
        "introduction": "Committees examine issues in more detail and may review bills, hear evidence or invite public submissions, depending on their mandate.",
        "sections": [
            {
                "heading": "Check the committee’s mandate",
                "body": "The committee’s mandate helps explain what topics it can consider and what work it is responsible for.",
            },
            {
                "heading": "Follow meetings and reports",
                "body": "Look for meeting notices, agendas, submissions, reports and recommendations in official parliamentary records.",
            },
            {
                "heading": "Understand recommendations",
                "body": "A committee report can inform what happens next, but recommendations and decisions should be checked against the official record.",
            },
        ],
        "takeaways": [
            "Committees focus on specific areas of parliamentary work.",
            "Meeting notices and reports can show what was discussed.",
            "Check what action followed a report or recommendation.",
        ],
        "sourceUrl": "https://www.parliament.go.ke/the-national-assembly/committees",
        "sourceName": "Parliament of Kenya",
        "next": "public-participation",
    },
    {
        "id": "public-participation",
        "topic": "Participation",
        "title": "Taking part in public participation",
        "description": "Understand how to find an invitation, prepare a submission and follow up.",
        "level": "Practical guide",
        "duration": "7 min",
        "icon": "message",
        "introduction": "Public participation gives people a way to share views on certain public decisions and proposals. Always check the official notice for the process and deadline.",
        "sections": [
            {
                "heading": "Find the official invitation",
                "body": "Look for the notice from Parliament, a committee or the relevant public body. Confirm the topic, deadline, venue or submission method.",
            },
            {
                "heading": "Prepare a focused submission",
                "body": "State the issue clearly, explain your reasons and identify the part of the proposal you are responding to. Keep a copy of what you submit.",
            },
            {
                "heading": "Follow what happens next",
                "body": "Check for committee reports, responses or other official records showing how the process moved forward.",
            },
        ],
        "takeaways": [
            "Confirm the deadline and instructions from the official notice.",
            "Refer to specific clauses or issues in your submission.",
            "Keep a copy and follow the official process afterward.",
        ],
        "sourceUrl": "https://www.parliament.go.ke/the-national-assembly/house-business/bills",
        "sourceName": "Parliament of Kenya",
        "next": "reading-bills",
    },
    {
        "id": "reading-bills",
        "topic": "Bills",
        "title": "How to read a bill",
        "description": "Learn to identify clauses, proposed changes and defined terms.",
        "level": "Practical guide",
        "duration": "5 min",
        "icon": "book",
        "introduction": "Bills use formal legal language and are divided into parts, clauses and schedules. A structured first read can help you identify what the proposal covers.",
        "sections": [
            {
                "heading": "Read the title and purpose",
                "body": "Start with the short title and any objects or purpose section. These provide context, but the operative clauses contain the proposed legal changes.",
            },
            {
                "heading": "Review definitions and clauses",
                "body": "Look for defined terms, who each clause applies to, and whether it creates a duty, power, offence, process or amendment.",
            },
            {
                "heading": "Compare proposed changes",
                "body": "If the bill amends an existing law, compare the bill text with the current law and verify the exact wording in both official sources.",
            },
        ],
        "takeaways": [
            "The title is a starting point; read the actual clauses.",
            "Pay attention to definitions and who the clause applies to.",
            "Check amendments against the current law.",
        ],
        "sourceUrl": "https://www.parliament.go.ke/the-national-assembly/house-business/bills",
        "sourceName": "Parliament of Kenya",
        "next": "checking-sources",
    },
    {
        "id": "checking-sources",
        "topic": "Research skills",
        "title": "How to check the source behind an explanation",
        "description": "Check article numbers, bill clauses and official parliamentary records.",
        "level": "Beginner",
        "duration": "3 min",
        "icon": "external",
        "introduction": "A reliable civic explanation should make it easy to find the original article, bill clause, debate or committee record it describes.",
        "sections": [
            {
                "heading": "Look for a precise reference",
                "body": "Check whether the explanation gives an article number, clause, bill number, date or parliamentary record reference.",
            },
            {
                "heading": "Open the original record",
                "body": "Follow the link to the official source and confirm that it supports the explanation. Check that you are looking at the right version and date.",
            },
            {
                "heading": "Notice what is uncertain",
                "body": "If a source is missing, outdated or unclear, treat the explanation cautiously and seek a verified record before relying on it.",
            },
        ],
        "takeaways": [
            "Prefer direct links to official records.",
            "Check dates and versions, especially for bills that are changing.",
            "A summary should not claim more than its cited source supports.",
        ],
        "sourceUrl": "https://www.parliament.go.ke/the-national-assembly/house-business/bills",
        "sourceName": "Parliament of Kenya",
        "next": "constitution-rights",
    },
]


def seed_initial_content() -> None:
    for lesson in LESSONS:
        seed_record_if_missing("lesson", lesson)
