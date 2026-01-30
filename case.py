import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Case Study Dashboard",
    layout="wide"
)

# --------------------------------------------------
# GLOBAL CSS (CLEAN, HIGH CONTRAST, NO SIDEBAR)
# --------------------------------------------------
st.markdown(
    """
    <style>

    * {
        font-family: "Times New Roman", Times, serif !important;
    }

    .stApp {
        background-color: #f2f4f8;
    }

    hr {
        display: none;
    }

    /* PAGE TITLE */
    .page-title {
        font-size: 34px;
        font-weight: 700;
        color: #111111;
        margin-bottom: 6px;
    }

    .page-subtitle {
        font-size: 17px;
        color: #4a4a4a;
        margin-bottom: 30px;
    }

    /* SECTION TITLE */
    .section-title {
        font-size: 22px;
        font-weight: 600;
        color: #111111;
        margin-bottom: 12px;
    }

    /* CARD */
    .card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        margin-bottom: 30px;
    }

    /* BODY TEXT */
    .body-text {
        font-size: 16px;
        line-height: 1.75;
        color: #222222;
    }

    /* PLACEHOLDER */
    .placeholder {
        background-color: #fafafa;
        border: 2px dashed #bdbdbd;
        border-radius: 8px;
        padding: 70px;
        text-align: center;
        font-size: 16px;
        color: #555555;
    }

    /* ---------- TABS STYLING ---------- */

    /* Tab container */
    div[data-baseweb="tab-list"] {
        background-color: #e6e9f0;
        padding: 6px;
        border-radius: 10px;
    }

    /* All tabs */
    button[data-baseweb="tab"] {
        font-size: 16px;
        font-weight: 600;
        padding: 10px 18px;
        color: #1f2937;              /* dark text */
        background-color: #f9fafb;   /* light background */
        border-radius: 8px;
        border: none;
    }

    /* Hover */
    button[data-baseweb="tab"]:hover {
        background-color: #dbeafe;
        color: #1e3a8a;
    }

    /* Active tab */
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #e5e7eb;   /* light grey */
        color: #111827;              /* dark text */
        box-shadow: 0 3px 8px rgba(0,0,0,0.12);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# TOP NAVIGATION (TABS)
# --------------------------------------------------
tabs = st.tabs([
    "Overview",
    "Sales Analysis",
    "Customer Insights",
    "Operational Metrics",
    "Random Forest Model"
])

# --------------------------------------------------
# OVERVIEW
# --------------------------------------------------
with tabs[0]:
    st.markdown("<div class='page-title'>Business Overview</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>High-level summary and problem context</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
            <div class='section-title'>Executive Summary</div>
            <div class='body-text'>
                This section introduces the business problem, defines the scope of the analysis,
                and outlines the approach taken across exploratory analysis and predictive modeling.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='card'>
            <div class='section-title'>Overview Dashboard</div>
            <div class='placeholder'>Place Tableau overview dashboard here</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# SALES ANALYSIS
# --------------------------------------------------
with tabs[1]:
    st.markdown("<div class='page-title'>Sales Analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Revenue trends and performance drivers</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
            <div class='section-title'>Sales Performance</div>
            <div class='placeholder'>Place Tableau sales visualizations here</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# CUSTOMER INSIGHTS
# --------------------------------------------------
with tabs[2]:
    st.markdown("<div class='page-title'>Customer Insights</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Segmentation and behavioral analysis</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
            <div class='section-title'>Customer Analysis</div>
            <div class='placeholder'>Place Tableau customer insights here</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# OPERATIONAL METRICS
# --------------------------------------------------
with tabs[3]:
    st.markdown("<div class='page-title'>Operational Metrics</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Efficiency and operational KPIs</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
            <div class='section-title'>Operations Dashboard</div>
            <div class='placeholder'>Place Tableau operational metrics here</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# RANDOM FOREST MODEL
# --------------------------------------------------
with tabs[4]:
    st.markdown("<div class='page-title'>Random Forest Model</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Predictive modeling and interpretation</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
            <div class='section-title'>Model Objective</div>
            <div class='body-text'>
                A Random Forest model is used to capture non-linear relationships
                and interactions between business variables to predict key outcomes.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='card'>
            <div class='section-title'>Model Outputs</div>
            <div class='placeholder'>
                Feature importance<br>
                Model performance metrics<br>
                Predictions and business interpretation
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
