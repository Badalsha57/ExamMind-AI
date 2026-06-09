from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_pdf(questions, output_file):

    doc = SimpleDocTemplate(output_file)

    styles = getSampleStyleSheet()

    story = []

    # Title
    title = Paragraph(
        "AI GENERATED QUESTION BANK",
        styles["Title"]
    )

    story.append(title)
    story.append(Spacer(1, 20))

    # Questions Section
    lines = questions.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Heading formatting
        if "LONG QUESTIONS" in line.upper():

            story.append(
                Paragraph(
                    "<b>LONG QUESTIONS</b>",
                    styles["Heading2"]
                )
            )

            story.append(Spacer(1, 10))

        elif "SHORT QUESTIONS" in line.upper():

            story.append(
                Paragraph(
                    "<b>SHORT QUESTIONS</b>",
                    styles["Heading2"]
                )
            )

            story.append(Spacer(1, 10))

        else:

            story.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            story.append(
                Spacer(1, 5)
            )

    # Build PDF
    doc.build(story)

    print(f"\nPDF Saved Successfully: {output_file}")