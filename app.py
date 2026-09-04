import gradio as gr
import pandas as pd


# ============================================================
# SAMPLE LEADERBOARD DATA
# ============================================================

students = [
    {"Rank": 1, "Student": "Rahul Sharma", "College": "IIT Delhi", "Earnings": 52400, "Change": 3},
    {"Rank": 2, "Student": "Ananya Roy", "College": "IIT Bombay", "Earnings": 47850, "Change": 1},
    {"Rank": 3, "Student": "Arjun Mehta", "College": "BITS Pilani", "Earnings": 41200, "Change": -1},
    {"Rank": 4, "Student": "Aditi Singh", "College": "IIT Delhi", "Earnings": 38200, "Change": 2},
    {"Rank": 5, "Student": "Rohan Das", "College": "VIT Vellore", "Earnings": 36850, "Change": -1},
    {"Rank": 6, "Student": "Sneha Patel", "College": "IIT Madras", "Earnings": 34200, "Change": 4},
    {"Rank": 7, "Student": "Kunal Verma", "College": "NIT Trichy", "Earnings": 31900, "Change": 0},
    {"Rank": 8, "Student": "Priya Shah", "College": "SRM University", "Earnings": 29850, "Change": 2},
    {"Rank": 9, "Student": "Aditya Jain", "College": "DTU", "Earnings": 27600, "Change": -2},
    {"Rank": 10, "Student": "Meera Nair", "College": "IIT Hyderabad", "Earnings": 25400, "Change": 1},

    {"Rank": 11, "Student": "Ishaan Gupta", "College": "IIIT Bangalore", "Earnings": 23100, "Change": 3},
    {"Rank": 12, "Student": "Neha Kapoor", "College": "NIT Warangal", "Earnings": 21800, "Change": -1},
    {"Rank": 13, "Student": "Vivek Rao", "College": "BITS Goa", "Earnings": 20450, "Change": 2},
    {"Rank": 14, "Student": "Tanya Bose", "College": "Jadavpur University", "Earnings": 19100, "Change": 0},
    {"Rank": 15, "Student": "Aman Khan", "College": "Manipal University", "Earnings": 18250, "Change": 1},
    {"Rank": 16, "Student": "Riya Sen", "College": "IIT Kanpur", "Earnings": 17600, "Change": -2},
    {"Rank": 17, "Student": "Dev Malhotra", "College": "NIT Rourkela", "Earnings": 16800, "Change": 2},
    {"Rank": 18, "Student": "Simran Kaur", "College": "Thapar University", "Earnings": 15900, "Change": 1},
    {"Rank": 19, "Student": "Varun Kumar", "College": "KIIT", "Earnings": 14800, "Change": -1},
    {"Rank": 20, "Student": "Nikhil Roy", "College": "IIT Kharagpur", "Earnings": 13900, "Change": 2},

    {
        "Rank": 47,
        "Student": "Jishan",
        "College": "IIIT Kalyani",
        "Earnings": 8450,
        "Change": 6
    }
]

df = pd.DataFrame(students)


# ============================================================
# FORMATTING
# ============================================================

def format_currency(value):
    return f"₹{value:,.0f}"


def get_change(change):
    if change > 0:
        return f'<span class="up">↑ {change}</span>'

    elif change < 0:
        return f'<span class="down">↓ {abs(change)}</span>'

    return '<span class="same">—</span>'


# ============================================================
# LEADERBOARD RENDERER
# ============================================================

def render_leaderboard(mode):

    data = df.copy()

    # --------------------------------------------------------
    # Filters
    # --------------------------------------------------------

    if mode == "This Week":

        # Simulated weekly leaderboard
        data = data.sort_values(
            by="Earnings",
            ascending=False
        ).reset_index(drop=True)

    elif mode == "My College":

        data = data[
            data["College"] == "IIIT Kalyani"
        ]

    # --------------------------------------------------------
    # Top 3
    # --------------------------------------------------------

    top3 = data.head(3)

    podium_html = ""

    medals = ["🥇", "🥈", "🥉"]

    for i, (_, row) in enumerate(top3.iterrows()):

        podium_html += f"""
        <div class="podium-card">

            <div class="medal">
                {medals[i]}
            </div>

            <div class="avatar">
                {row['Student'][0]}
            </div>

            <div class="podium-name">
                {row['Student']}
            </div>

            <div class="college">
                {row['College']}
            </div>

            <div class="podium-money">
                {format_currency(row['Earnings'])}
            </div>

        </div>
        """

    # --------------------------------------------------------
    # Leaderboard table
    # --------------------------------------------------------

    table_rows = ""

    for _, row in data.iterrows():

        is_user = row["Student"] == "Jishan"

        row_class = "user-row" if is_user else ""

        table_rows += f"""
        <tr class="{row_class}">

            <td class="rank">
                #{row['Rank']}
            </td>

            <td>

                <div class="student">

                    <div class="small-avatar">
                        {row['Student'][0]}
                    </div>

                    <div>

                        <strong class="student-name">
                            {row['Student']}

                            {" <span class='you'>YOU</span>" if is_user else ""}

                        </strong>

                        <div class="college">
                            {row['College']}
                        </div>

                    </div>

                </div>

            </td>

            <td class="money">
                {format_currency(row['Earnings'])}
            </td>

            <td>
                {get_change(row['Change'])}
            </td>

        </tr>
        """

    # ========================================================
    # MAIN HTML
    # ========================================================

    html = f"""

    <div class="leaderboard-container">

        <!-- ==================================================
             HERO
        =================================================== -->

        <div class="top-section">

            <div class="orange-circle"></div>

            <div class="eyebrow">
                EYFI CHALLENGE
            </div>

            <h1>
                India's Student<br>
                <span>Earning Movement.</span>
            </h1>

            <p class="subtitle">
                See who's earning, climbing and making their first income.
            </p>


            <!-- TOTAL EARNINGS -->

            <div class="total-card">

                <div>

                    <div class="total-label">
                        TOTAL EARNED BY STUDENTS
                    </div>

                    <div class="total-value">
                        ₹12,84,500
                    </div>

                </div>


                <div class="student-count">

                    <strong>
                        2,481
                    </strong>

                    <br>

                    students earning

                </div>

            </div>

        </div>


        <!-- ==================================================
             YOUR RANK
        =================================================== -->

        <div class="your-rank">

            <div class="your-rank-main">

                <div class="your-label">
                    YOUR RANK
                </div>

                <div class="your-rank-number">
                    #47
                </div>

            </div>


            <div class="your-stat">

                <div class="stat-label">
                    YOUR EARNINGS
                </div>

                <div class="stat-value">
                    ₹8,450
                </div>

            </div>


            <div class="your-stat">

                <div class="stat-label">
                    THIS WEEK
                </div>

                <div class="stat-value green">
                    ↑ 6 places
                </div>

            </div>

        </div>


        <!-- ==================================================
             TOP EARNERS
        =================================================== -->

        <div class="section-title">
            Top Earners
        </div>

        <div class="podium">

            {podium_html}

        </div>


        <!-- ==================================================
             LEADERBOARD HEADER
        =================================================== -->

        <div class="leaderboard-header">

            <div>

                <div class="section-title">
                    Leaderboard
                </div>

                <div class="muted">
                    Keep earning. Keep climbing.
                </div>

            </div>

        </div>


        <!-- ==================================================
             TABLE
        =================================================== -->

        <div class="table-wrapper">

            <table>

                <thead>

                    <tr>

                        <th>
                            RANK
                        </th>

                        <th>
                            STUDENT
                        </th>

                        <th>
                            EARNINGS
                        </th>

                        <th>
                            CHANGE
                        </th>

                    </tr>

                </thead>


                <tbody>

                    {table_rows}

                </tbody>

            </table>

        </div>

    </div>

    """

    return html


# ============================================================
# CSS
# ============================================================

css = """

/* ============================================================
   GLOBAL
============================================================ */

* {
    font-family: Inter, Arial, sans-serif;
}

body {
    background: #FFF8F3;
    color: #171717;
}

.gradio-container {
    max-width: 1150px !important;
    margin: auto;
}

.leaderboard-container {
    padding: 30px;
    color: #171717;
}


/* ============================================================
   HEADER / HERO
============================================================ */

.top-section {

    background: #FFFFFF;

    color: #171717;

    border-radius: 28px;

    padding: 45px;

    margin-bottom: 22px;

    position: relative;

    overflow: hidden;

    border: 1px solid #F0E7DF;

    box-shadow:
        0 8px 30px rgba(0, 0, 0, 0.05);
}


/* Orange decorative circle */

.orange-circle {

    position: absolute;

    width: 220px;

    height: 220px;

    background: #FF6B00;

    border-radius: 50%;

    right: -80px;

    top: -90px;

    opacity: 0.12;

}


/* Small orange accent */

.top-section:before {

    content: "";

    position: absolute;

    width: 7px;

    height: 70px;

    background: #FF6B00;

    border-radius: 10px;

    left: 0;

    top: 45px;
}


/* EYFI CHALLENGE */

.eyebrow {

    color: #FF6B00;

    font-size: 13px;

    font-weight: 800;

    letter-spacing: 2px;

    position: relative;

    z-index: 2;
}


/* Main heading */

h1 {

    color: #171717;

    font-size: 46px;

    line-height: 1.05;

    margin: 15px 0;

    letter-spacing: -2px;

    position: relative;

    z-index: 2;
}


/* Orange heading text */

h1 span {

    color: #FF6B00;
}


/* Subtitle */

.subtitle {

    color: #666666;

    font-size: 16px;

    margin-bottom: 35px;

    position: relative;

    z-index: 2;
}


/* ============================================================
   TOTAL EARNINGS CARD
============================================================ */

.total-card {

    display: flex;

    justify-content: space-between;

    align-items: center;

    background: #FFF8F3;

    border: 1px solid #F4D8C3;

    border-radius: 18px;

    padding: 20px 25px;

    max-width: 600px;

    position: relative;

    z-index: 2;
}


/* Label */

.total-label {

    color: #777777;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 1px;
}


/* Main total earnings */

.total-value {

    color: #171717;

    font-size: 32px;

    font-weight: 900;

    margin-top: 5px;
}


/* Student count */

.student-count {

    color: #777777;

    text-align: right;
}


/* Student count number */

.student-count strong {

    color: #171717;

    font-size: 20px;
}


/* ============================================================
   YOUR RANK
============================================================ */

.your-rank {

    display: flex;

    align-items: center;

    gap: 55px;

    background: #FFFFFF;

    color: #171717;

    border-radius: 20px;

    padding: 25px 30px;

    margin-bottom: 35px;

    border: 2px solid #FF6B00;

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.06);
}


/* Your rank */

.your-rank-main {

    min-width: 120px;
}


.your-label {

    color: #777777;

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1px;
}


.your-rank-number {

    color: #171717;

    font-size: 34px;

    font-weight: 900;
}


/* Stats */

.your-stat {

    min-width: 130px;
}


.stat-label {

    color: #777777;

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1px;
}


.stat-value {

    color: #171717;

    font-size: 22px;

    font-weight: 900;
}


/* Positive movement */

.green {

    color: #16A34A !important;
}


/* ============================================================
   SECTION TITLES
============================================================ */

.section-title {

    color: #171717;

    font-size: 24px;

    font-weight: 850;

    margin-bottom: 4px;
}


.muted {

    color: #777777;

    font-size: 13px;
}


/* ============================================================
   PODIUM
============================================================ */

.podium {

    display: grid;

    grid-template-columns: repeat(3, 1fr);

    gap: 15px;

    margin: 20px 0 40px;
}


.podium-card {

    background: #FFFFFF;

    color: #171717;

    border-radius: 20px;

    padding: 25px;

    text-align: center;

    border: 1px solid #F0E7DF;

    transition: all 0.2s ease;

    box-shadow:
        0 4px 15px rgba(0, 0, 0, 0.03);
}


.podium-card:hover {

    transform: translateY(-5px);

    border-color: #FF6B00;

    box-shadow:
        0 12px 30px rgba(0, 0, 0, 0.08);
}


/* Medal */

.medal {

    font-size: 30px;
}


/* Avatar */

.avatar {

    width: 55px;

    height: 55px;

    background: #FFF0E6;

    color: #FF6B00;

    border-radius: 50%;

    margin: 10px auto;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 22px;

    font-weight: 900;
}


/* Student name */

.podium-name {

    color: #171717;

    font-weight: 850;

    font-size: 16px;
}


/* College */

.college {

    color: #666666;

    font-size: 12px;

    margin-top: 3px;
}


/* Earnings */

.podium-money {

    color: #171717;

    font-size: 20px;

    font-weight: 900;

    margin-top: 12px;
}


/* ============================================================
   LEADERBOARD TABLE
============================================================ */

.leaderboard-header {

    margin-bottom: 15px;
}


.table-wrapper {

    background: #FFFFFF;

    border-radius: 20px;

    overflow: hidden;

    border: 1px solid #F0E7DF;

    box-shadow:
        0 5px 20px rgba(0, 0, 0, 0.03);
}


table {

    width: 100%;

    border-collapse: collapse;

    color: #171717;
}


/* Table headers */

th {

    text-align: left;

    font-size: 10px;

    letter-spacing: 1px;

    color: #666666;

    padding: 16px 20px;

    background: #FAFAFA;

    font-weight: 800;
}


/* Table cells */

td {

    padding: 15px 20px;

    border-top: 1px solid #F2F2F2;

    color: #171717;
}


/* Rank */

.rank {

    color: #171717;

    font-weight: 900;

    width: 90px;
}


/* Student */

.student {

    display: flex;

    align-items: center;

    gap: 12px;
}


/* Student name */

.student-name {

    color: #171717;

    font-weight: 800;
}


/* Small avatar */

.small-avatar {

    width: 38px;

    height: 38px;

    background: #FFF0E6;

    color: #FF6B00;

    border-radius: 50%;

    display: flex;

    align-items: center;

    justify-content: center;

    font-weight: 900;
}


/* Earnings */

.money {

    color: #171717;

    font-weight: 900;

    font-size: 15px;
}


/* ============================================================
   RANK MOVEMENT
============================================================ */

.up {

    color: #16A34A;

    font-weight: 800;
}


.down {

    color: #DC2626;

    font-weight: 800;
}


.same {

    color: #777777;
}


/* ============================================================
   USER ROW
============================================================ */

.user-row {

    background: #FFF3EA;

    box-shadow:
        inset 4px 0 #FF6B00;
}


.user-row .rank {

    color: #171717;
}


.user-row .student-name {

    color: #171717;
}


.user-row .money {

    color: #171717;
}


/* YOU badge */

.you {

    background: #FF6B00;

    color: #FFFFFF;

    border-radius: 5px;

    padding: 3px 6px;

    font-size: 9px;

    margin-left: 5px;

    font-weight: 800;
}


/* ============================================================
   GRADIO RADIO BUTTONS
============================================================ */

.gradio-radio {

    margin-bottom: 20px;
}


.gradio-radio label {

    color: #171717 !important;

    font-weight: 700 !important;
}


/* ============================================================
   RESPONSIVE
============================================================ */

@media(max-width: 700px) {

    .leaderboard-container {

        padding: 12px;
    }


    .top-section {

        padding: 30px 22px;
    }


    h1 {

        font-size: 35px;
    }


    .total-card {

        display: block;
    }


    .student-count {

        text-align: left;

        margin-top: 15px;
    }


    .your-rank {

        gap: 20px;

        flex-wrap: wrap;
    }


    .your-rank-main {

        min-width: 100px;
    }


    .podium {

        grid-template-columns: 1fr;
    }


    table th:nth-child(2),
    table td:nth-child(2) {

        min-width: 180px;
    }

}

"""


# ============================================================
# GRADIO APP
# ============================================================

with gr.Blocks(
    title="EYFI Challenge Leaderboard",
    css=css,
    theme=gr.themes.Base()
) as demo:

    # --------------------------------------------------------
    # Top Navigation
    # --------------------------------------------------------

    gr.HTML("""
    <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        padding:10px 10px 20px;
    ">

        <div style="
            font-size:25px;
            font-weight:900;
            color:#FF6B00;
        ">
            EYFI
        </div>


        <div style="
            font-size:13px;
            color:#666666;
        ">
            Earn Your First Income
        </div>

    </div>
    """)


    # --------------------------------------------------------
    # Leaderboard Filter
    # --------------------------------------------------------

    mode = gr.Radio(
        ["Overall", "This Week", "My College"],
        value="Overall",
        label="View"
    )


    # --------------------------------------------------------
    # Leaderboard
    # --------------------------------------------------------

    leaderboard = gr.HTML(
        value=render_leaderboard("Overall")
    )


    # --------------------------------------------------------
    # Update leaderboard when filter changes
    # --------------------------------------------------------

    mode.change(
        fn=render_leaderboard,
        inputs=mode,
        outputs=leaderboard
    )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    demo.launch()