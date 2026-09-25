import streamlit as st
from services.persistence.exercise_repository import get_or_create_user


def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True

    st.session_state.appearance_mode = "light"

    st.markdown(
        f'<div class="login-theme login-theme-{st.session_state.appearance_mode}"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <section class="login-shell">
            <div class="login-brand-row">
                <div class="brand-mark">RS</div>
                <span class="brand-name">REPSENSE <b>AI</b></span>
                <span class="brand-status"><i></i> LIVE COACHING</span>
            </div>
            <div class="login-hero">
                <p class="login-kicker">YOUR FORM. YOUR PACE. YOUR COACH.</p>
                <h1>Train with<br><em>intent.</em></h1>
                <p class="login-copy">
                    Real-time movement tracking and intelligent feedback for stronger,
                    safer sessions.
                </p>
            </div>
            <div class="login-feature-strip">
                <span><strong>01</strong> Pose tracking</span>
                <span><strong>02</strong> Live corrections</span>
                <span><strong>03</strong> Session history</span>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<p class=\"login-form-heading\">Start your training profile</p>", unsafe_allow_html=True)

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("YOUR NAME", placeholder="e.g. Aman")
        submit_button = st.form_submit_button("Start Session", width="stretch")

    if submit_button:
        if not username:
            st.error("Name cannot be empty.")
            return False
        
        user = get_or_create_user(username)
    
        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]

        st.rerun()

    return False