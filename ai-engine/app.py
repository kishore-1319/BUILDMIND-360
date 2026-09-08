import streamlit as st

from llm.analyzer import analyze_feedback


st.set_page_config(
    page_title="BUILDMIND-360 AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 BUILDMIND-360")
st.subheader("AI Feedback Intelligence Engine")

feedback = st.text_area(
    "Enter customer feedback",
    height=200,
    placeholder="Example: The app crashes whenever I try to make a payment..."
)

if st.button("Analyze Feedback"):

    if not feedback.strip():

        st.warning("Please enter customer feedback.")

    else:

        try:

            with st.spinner("BUILDMIND-360 is analyzing..."):

                result = analyze_feedback(feedback)

            st.success("Analysis completed.")

            st.markdown("## Customer Problem")
            st.write(result.customer_problem)

            st.markdown("## Issue")
            st.write(result.issue)

            st.markdown("## Affected Feature")
            st.write(result.affected_feature)

            st.markdown("## Severity")
            st.write(result.severity)

            st.markdown("## Priority")
            st.write(result.priority)

            st.markdown("## Customer Impact")
            st.write(result.customer_impact)

            st.markdown("## Possible Root Cause")
            st.write(result.root_cause_hypothesis)

            st.markdown("## Recommended Solution")
            st.write(result.recommended_solution)

            st.markdown("## What Should Be Developed Next?")
            st.write(result.development_action)

            st.markdown("## Engineering Action")
            st.write(result.engineering_action)

            st.markdown("## Product Action")
            st.write(result.product_action)

            st.markdown("## Support Action")
            st.write(result.support_action)

            st.markdown("## Confidence")
            st.write(result.confidence)

            with st.expander("Complete AI JSON"):
                st.json(result.model_dump())

        except Exception as e:

            st.error("Analysis failed.")
            st.exception(e)