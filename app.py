import gradio as gr
import pandas as pd


# -----------------------------
# Sample leaderboard data
# -----------------------------

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


# -----------------------------
# Formatting
# -----------------------------

def format_currency(value):
    return f"₹{value:,.0f}"


def get_change(change):
    if change > 0:
        return f'<span class="up">↑ {change}</span>'
    elif change < 0:
        return f'<span class="down">↓ {abs(change)}</span>'
    return '<span class="same">—</span>'


# -----------------------------
# Leaderboard renderer
# -----------------------------

def render_leaderboard(mode):

    data = df.copy()

    if mode == "This Week":
        # Simulated weekly ordering
        data = data.sort_values(
            by="Earnings",
            ascending=False
        ).reset_index(drop=True)

    elif mode == "My College":
        data = data[data["College"] == "IIIT Kalyani"]

    # Top 3
    top3 = data.head(3)

    podium_html = ""

    medals = ["🥇", "🥈", "🥉"]

    for i, (_, row) in enumerate(top3.iterrows()):

        podium_html += f"""
        <div class="podium-card">
            <div class="medal">{medals[i]}</div>
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

    # Table
    table_rows = ""

    for _, row in data.iterrows():

        is_user = row["Student"] == "Jishan"

        row_class = "user-row" if is_user else ""

        table_rows += f"""
        <tr class="{row_class}">
            <td class="rank">#{row['Rank']}</td>

            <td>
                <div class="student">
                    <div class="small-avatar">
                        {row['Student'][0]}
                    </div>

                    <div>
                        <strong>
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

    html = f"""
    <div class="leaderboard-container">

        <div class="top-section">

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
                    <strong>2,481</strong>
                    <br>
                    students earning
                </div>

            </div>

        </div>


        <div class="your-rank">

            <div>
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


        <div class="section-title">
            Top Earners
        </div>

        <div class="podium">
            {podium_html}
        </div>


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


        <div class="table-wrapper">

            <table>

                <thead>
                    <tr>
                        <th>RANK</th>
                        <th>STUDENT</th>
                        <th>EARNINGS</th>
                        <th>CHANGE</th>
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


# -----------------------------
# CSS
# -----------------------------

css = """

* {
    font-family: Inter, Arial, sans-serif;
}

body {
    background: #FFF8F3;
}

.gradio-container {
    max-width: 1150px !important;
    margin: auto;
}

.leaderboard-container {
    padding: 30px;
    color: #171717;
}

/* HERO */

.top-section {
    background: #171717;
    color: white;
    border-radius: 28px;
    padding: 45px;
    margin-bottom: 22px;
    position: relative;
    overflow: hidden;
}

.top-section:after {
    content: "";
    position: absolute;
    width: 250px;
    height: 250px;
    background: #FF6B00;
    border-radius: 50%;
    right: -80px;
    top: -80px;
    opacity: 0.9;
}

.eyebrow {
    color: #FF8A3D;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 2px;
}

h1 {
    font-size: 46px;
    line-height: 1.05;
    margin: 15px 0;
    letter-spacing: -2px;
}

h1 span {
    color: #FF6B00;
}

.subtitle {
    color: #BDBDBD;
    font-size: 16px;
    margin-bottom: 35px;
}

.total-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 18px;
    padding: 20px 25px;
    max-width: 600px;
}

.total-label {
    color: #BDBDBD;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
}

.total-value {
    font-size: 32px;
    font-weight: 800;
    margin-top: 5px;
}

.student-count {
    color: #BDBDBD;
    text-align: right;
}

.student-count strong {
    color: white;
    font-size: 20px;
}


/* YOUR RANK */

.your-rank {
    display: flex;
    align-items: center;
    gap: 55px;
    background: #FF6B00;
    color: white;
    border-radius: 20px;
    padding: 25px 30px;
    margin-bottom: 35px;
    box-shadow: 0 10px 30px rgba(255,107,0,0.18);
}

.your-label,
.stat-label {
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
    opacity: 0.8;
}

.your-rank-number {
    font-size: 34px;
    font-weight: 900;
}

.stat-value {
    font-size: 22px;
    font-weight: 800;
}

.green {
    color: #E8FFE8;
}


/* PODIUM */

.section-title {
    font-size: 24px;
    font-weight: 850;
    margin-bottom: 4px;
}

.muted {
    color: #888;
    font-size: 13px;
}

.podium {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
    margin: 20px 0 40px;
}

.podium-card {
    background: white;
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    border: 1px solid #F0E7DF;
    transition: 0.2s;
}

.podium-card:hover {
    transform: translateY(-5px);
    border-color: #FF6B00;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
}

.medal {
    font-size: 30px;
}

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

.podium-name {
    font-weight: 800;
    font-size: 16px;
}

.college {
    color: #888;
    font-size: 12px;
    margin-top: 3px;
}

.podium-money {
    color: #FF6B00;
    font-size: 20px;
    font-weight: 900;
    margin-top: 12px;
}


/* TABLE */

.leaderboard-header {
    margin-bottom: 15px;
}

.table-wrapper {
    background: white;
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid #F0E7DF;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th {
    text-align: left;
    font-size: 10px;
    letter-spacing: 1px;
    color: #999;
    padding: 16px 20px;
    background: #FAFAFA;
}

td {
    padding: 15px 20px;
    border-top: 1px solid #F2F2F2;
}

.rank {
    font-weight: 800;
    width: 90px;
}

.student {
    display: flex;
    align-items: center;
    gap: 12px;
}

.small-avatar {
    width: 38px;
    height: 38px;
    background: #FFF0E6;
    color: #FF6B00;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
}

.money {
    font-weight: 850;
}

.up {
    color: #16A34A;
    font-weight: 800;
}

.down {
    color: #DC2626;
    font-weight: 800;
}

.same {
    color: #999;
}

.user-row {
    background: #FFF3EA;
    box-shadow: inset 4px 0 #FF6B00;
}

.you {
    background: #FF6B00;
    color: white;
    border-radius: 5px;
    padding: 3px 6px;
    font-size: 9px;
    margin-left: 5px;
}


/* RESPONSIVE */

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

    .podium {
        grid-template-columns: 1fr;
    }

    table th:nth-child(2),
    table td:nth-child(2) {
        min-width: 180px;
    }
}

"""


# -----------------------------
# Gradio App
# -----------------------------

with gr.Blocks(
    title="EYFI Challenge Leaderboard",
    css=css,
    theme=gr.themes.Base()
) as demo:

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
            color:#777;
        ">
            Earn Your First Income
        </div>
    </div>
    """)

    mode = gr.Radio(
        ["Overall", "This Week", "My College"],
        value="Overall",
        label="View"
    )

    leaderboard = gr.HTML(
        value=render_leaderboard("Overall")
    )

    mode.change(
        fn=render_leaderboard,
        inputs=mode,
        outputs=leaderboard
    )


if __name__ == "__main__":
    demo.launch()