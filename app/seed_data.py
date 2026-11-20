from typing import Any

from app.database import seed_record_if_missing


CONSTITUTION_SOURCE_URL = (
    "https://www.parliament.go.ke/sites/default/files/2017-05/"
    "The_Constitution_of_Kenya_2010.pdf"
)

CONSTITUTION_SECTIONS: list[dict[str, Any]] = [
    {
        "id": "article-22",
        "number": 22,
        "title": "Enforcement of the Bill of Rights",
        "titleSw": "Utekelezaji wa Mswada wa Haki",
        "excerpt": (
            "22. (1) Every person has the right to institute court proceedings "
            "claiming that a right or fundamental freedom in the Bill of Rights "
            "has been denied, violated or infringed, or is threatened."
        ),
        "plainLanguage": (
            "You can ask a court to consider a claim that a right or fundamental "
            "freedom has been denied, violated, infringed or is threatened. This "
            "provides a way to seek legal protection; it does not mean every "
            "claim will succeed."
        ),
        "plainLanguageSw": (
            "Unaweza kuiomba mahakama isikilize madai kwamba haki au uhuru wa "
            "kimsingi umenyimwa, umekiukwa, umeingiliwa au uko hatarini. Hii "
            "hutoa njia ya kutafuta ulinzi wa kisheria; haimaanishi kwamba kila "
            "dai litafaulu."
        ),
        "howItHelps": (
            "If you believe a Bill of Rights protection is being threatened or "
            "breached, Article 22 recognizes a route to bring the issue before "
            "a court. Consider qualified legal help for your situation."
        ),
        "howItHelpsSw": (
            "Ukidhani kwamba haki iliyo kwenye Mswada wa Haki inatishiwa au "
            "imekiukwa, Kifungu cha 22 kinatambua njia ya kuwasilisha suala hilo "
            "mahakamani. Tafuta msaada wa kisheria unaofaa kwa hali yako."
        ),
    },
    {
        "id": "article-35",
        "number": 35,
        "title": "Access to information",
        "titleSw": "Upatikanaji wa taarifa",
        "excerpt": (
            "35. (1) Every citizen has the right of access to— (a) information "
            "held by the State; and (b) information held by another person and "
            "required for the exercise or protection of any right or fundamental "
            "freedom. (2) Every person has the right to the correction or deletion "
            "of untrue or misleading information that affects the person."
        ),
        "plainLanguage": (
            "Citizens may access information held by the State, and information "
            "held by another person when it is needed to exercise or protect a "
            "right or freedom. Everyone can seek correction or deletion of "
            "untrue or misleading information that affects them."
        ),
        "plainLanguageSw": (
            "Wananchi wanaweza kupata taarifa zinazoshikiliwa na Serikali, na "
            "taarifa za mtu mwingine zinapohitajika kutekeleza au kulinda haki "
            "au uhuru. Kila mtu anaweza kuomba taarifa zisizo za kweli au "
            "zinazopotosha na zinazomhusu zirekebishwe au zifutwe."
        ),
        "howItHelps": (
            "You can ask for State-held information, or seek correction of "
            "misleading information that affects you. For information held by "
            "another person, the Constitution ties access to exercising or "
            "protecting a right or freedom."
        ),
        "howItHelpsSw": (
            "Unaweza kuomba taarifa zinazoshikiliwa na Serikali, au kuomba "
            "taarifa za kupotosha zinazokuhusu zirekebishwe. Kwa taarifa "
            "zinazoshikiliwa na mtu mwingine, Katiba inaunganisha upatikanaji "
            "wake na kutekeleza au kulinda haki au uhuru."
        ),
    },
    {
        "id": "article-43",
        "number": 43,
        "title": "Economic and social rights",
        "titleSw": "Haki za kiuchumi na kijamii",
        "excerpt": (
            "43. (1) Every person has the right— (a) to the highest attainable "
            "standard of health, which includes the right to health care services, "
            "including reproductive health care; (b) to accessible and adequate "
            "housing, and to reasonable standards of sanitation; (c) to be free "
            "from hunger, and to have adequate food of acceptable quality; "
            "(d) to clean and safe water in adequate quantities; (e) to social "
            "security; and (f) to education. (2) A person shall not be denied "
            "emergency medical treatment. (3) The State shall provide appropriate "
            "social security to persons who are unable to support themselves and "
            "their dependants."
        ),
        "plainLanguage": (
            "The Constitution recognizes rights relating to health care, "
            "accessible and adequate housing, food, clean water, social security "
            "and education. "
            "It also says emergency medical treatment must not be denied."
        ),
        "plainLanguageSw": (
            "Katiba inatambua haki zinazohusu huduma za afya, makazi "
            "yanayofikika na ya kutosha, chakula, maji safi, hifadhi ya jamii "
            "na elimu. Pia inasema matibabu ya dharura hayapaswi kukataliwa."
        ),
        "howItHelps": (
            "This gives you a constitutional reference when asking about "
            "essential services, and specifically protects access to emergency "
            "medical treatment. It does not determine the outcome of an "
            "individual service request."
        ),
        "howItHelpsSw": (
            "Kifungu hiki kinakupa rejea ya Katiba unapouliza kuhusu huduma "
            "muhimu, na kinalinda hasa upatikanaji wa matibabu ya dharura. "
            "Haki hii haiamui moja kwa moja matokeo ya ombi lako binafsi la "
            "huduma."
        ),
    },
    {
        "id": "article-47",
        "number": 47,
        "title": "Fair administrative action",
        "titleSw": "Hatua ya kiutawala ya haki",
        "excerpt": (
            "47. (1) Every person has the right to administrative action that is "
            "expeditious, efficient, lawful, reasonable and procedurally fair. "
            "(2) If a right or fundamental freedom of a person has been or is "
            "likely to be adversely affected by administrative action, the person "
            "has the right to be given written reasons for the action."
        ),
        "plainLanguage": (
            "Administrative action must be prompt, efficient, lawful, reasonable "
            "and procedurally fair. If it has or is likely to harm your right or "
            "freedom, you have a right to written reasons."
        ),
        "plainLanguageSw": (
            "Hatua za kiutawala zinapaswa kuchukuliwa kwa wakati, kwa ufanisi, "
            "kwa mujibu wa sheria, kwa busara na kwa utaratibu wa haki. Ikiwa "
            "hatua hiyo imeathiri au huenda ikaathiri haki au uhuru wako, una "
            "haki ya kupewa sababu kwa maandishi."
        ),
        "howItHelps": (
            "If an administrative decision affects you, this article can help "
            "you ask for written reasons and understand that fair process "
            "matters. It does not decide whether a particular decision was lawful."
        ),
        "howItHelpsSw": (
            "Ikiwa uamuzi wa kiutawala unakuhusu, kifungu hiki kinaweza "
            "kukusaidia kuomba sababu kwa maandishi na kuelewa umuhimu wa "
            "utaratibu wa haki. Haki hii haiamui yenyewe kama uamuzi fulani "
            "ulikuwa halali."
        ),
    },
    {
        "id": "article-48",
        "number": 48,
        "title": "Access to justice",
        "titleSw": "Upatikanaji wa haki",
        "excerpt": (
            "48. The State shall ensure access to justice for all persons and, "
            "if any fee is required, it shall be reasonable and shall not impede "
            "access to justice."
        ),
        "plainLanguage": (
            "The State must ensure that everyone can access justice. Any fee "
            "required must be reasonable and must not block that access."
        ),
        "plainLanguageSw": (
            "Serikali inapaswa kuhakikisha kwamba kila mtu anaweza kupata "
            "haki. Ada yoyote inayohitajika inapaswa kuwa ya kiasi na "
            "isizuie upatikanaji wa haki."
        ),
        "howItHelps": (
            "When a fee is a barrier to a justice process, Article 48 provides "
            "a constitutional reference: the fee must be reasonable and must "
            "not impede access to justice. Ask a qualified legal aid provider "
            "about options for your circumstances."
        ),
        "howItHelpsSw": (
            "Ada inapokuwa kikwazo katika mchakato wa kutafuta haki, Kifungu "
            "cha 48 kinatoa rejea ya Katiba: ada inapaswa kuwa ya kiasi na "
            "isizuie upatikanaji wa haki. Uliza mtoa huduma ya msaada wa "
            "kisheria kuhusu chaguo zinazofaa hali yako."
        ),
    },
    {
        "id": "article-49",
        "number": 49,
        "title": "Rights of arrested persons",
        "titleSw": "Haki za watu waliokamatwa",
        "excerpt": (
            "49. (1) An arrested person has the right— (a) to be informed "
            "promptly, in language that the person understands, of— (i) the "
            "reason for the arrest; (ii) the right to remain silent; and (iii) the "
            "consequences of not remaining silent; (b) to remain silent; "
            "(c) to communicate with an advocate, and other persons whose "
            "assistance is necessary."
        ),
        "plainLanguage": (
            "An arrested person must be told promptly, in a language they "
            "understand, why they were arrested and about the right to remain "
            "silent. They also have a right to communicate with an advocate."
        ),
        "plainLanguageSw": (
            "Mtu aliyekamatwa anapaswa kuambiwa mara moja, kwa lugha "
            "anayoielewa, sababu ya kukamatwa na kuhusu haki ya kunyamaza. "
            "Pia ana haki ya kuwasiliana na wakili."
        ),
        "howItHelps": (
            "If you or someone with you is arrested, this article identifies "
            "rights to be informed of the reason, to remain silent and to "
            "communicate with an advocate. This is general civic information, "
            "not legal advice."
        ),
        "howItHelpsSw": (
            "Wewe au mtu aliye pamoja nawe akikamatwa, kifungu hiki kinaeleza "
            "haki ya kufahamishwa sababu, kunyamaza na kuwasiliana na wakili. "
            "Haya ni maelezo ya jumla ya uraia, si ushauri wa kisheria."
        ),
    },
]


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
    for section in CONSTITUTION_SECTIONS:
        seed_record_if_missing(
            "article",
            {
                **section,
                "sourceUrl": CONSTITUTION_SOURCE_URL,
                "sourceName": "Parliament of Kenya",
            },
        )

    for lesson in LESSONS:
        seed_record_if_missing("lesson", lesson)
