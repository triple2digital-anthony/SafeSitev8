import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

def generate_random_report():
    """Generates a randomized behavioral analysis report"""
    
    # Simulate processing time with a progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(100):
        progress_bar.progress(i + 1)
        if i < 30:
            status_text.text("Analyzing behavioral patterns...")
        elif i < 60:
            status_text.text("Generating insights...")
        elif i < 90:
            status_text.text("Compiling report...")
        else:
            status_text.text("Finalizing...")
        time.sleep(0.02)

    # Clear progress indicators
    progress_bar.empty()
    status_text.empty()

    # Generate random metrics
    isolation_trend = np.random.choice(['increasing', 'decreasing', 'stable'])
    risk_level = np.random.choice(['Low', 'Moderate', 'High'])
    interaction_score = round(np.random.uniform(60, 95), 1)
    alert_count = np.random.randint(0, 5)
    
    # Create report container
    report_container = st.container()
    
    with report_container:
        st.markdown("### 📊 Behavioral Analysis Report")
        st.markdown(f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
        
        # Key Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Risk Level", risk_level, 
                     delta="2% from last week" if risk_level == "Moderate" else None,
                     delta_color="inverse")
        with col2:
            st.metric("Social Interaction Score", f"{interaction_score}%",
                     delta=f"{np.random.randint(-5, 6)}% vs avg")
        with col3:
            st.metric("Active Alerts", alert_count,
                     delta=f"{np.random.randint(-2, 3)} from yesterday")

        # Detailed Insights
        st.markdown("#### 🔍 Key Insights")
        st.markdown(f"""
        * Social Isolation Trend: **{isolation_trend}** over the past 7 days
        * {np.random.randint(2, 6)} students showing unusual behavioral patterns
        * {np.random.randint(85, 99)}% of interactions are positive
        * {np.random.randint(2, 5)} potential intervention opportunities identified
        """)

        # Generate random weekly data
        dates = pd.date_range(end=datetime.now(), periods=7, freq='D')
        weekly_data = pd.DataFrame({
            'Date': dates,
            'Positive Interactions': np.random.randint(40, 100, 7),
            'Concerning Behaviors': np.random.randint(0, 20, 7),
            'Intervention Events': np.random.randint(0, 5, 7)
        })

        # Weekly Trends Chart
        st.markdown("#### 📈 Weekly Behavior Trends")
        fig = px.line(weekly_data, x='Date', 
                     y=['Positive Interactions', 'Concerning Behaviors', 'Intervention Events'],
                     title='7-Day Behavioral Pattern Analysis')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

        # Recommendations
        st.markdown("#### 🎯 Recommended Actions")
        recommendations = [
            "Schedule check-in with students showing isolation patterns",
            "Increase monitoring during identified peak times",
            "Review and adjust intervention thresholds",
            "Conduct focused observation during transition periods",
            "Update behavioral baseline metrics"
        ]
        np.random.shuffle(recommendations)
        for i, rec in enumerate(recommendations[:3], 1):
            st.markdown(f"{i}. {rec}")

        # Export options (simulated)
        st.markdown("#### 📑 Export Options")
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "Download Full Report (PDF)",
                data="Sample PDF content",
                file_name="behavioral_analysis_report.pdf",
                mime="application/pdf"
            )
        with col2:
            st.download_button(
                "Export Data (CSV)",
                data=weekly_data.to_csv(index=False),
                file_name="behavioral_data.csv",
                mime="text/csv"
            )

def show_behavioral_patterns():
    st.title("Behavioral Pattern Analysis")
    
    # Introduction and Context
    st.markdown("""
    ### Understanding Student Behavioral Patterns
    This analysis provides insights into student interactions, social dynamics, and potential risk factors 
    identified through our AI-powered monitoring system. The patterns shown here can help identify:
    
    - 🔍 Early warning signs of concerning behavior
    - 👥 Social dynamics and group formations
    - 📊 Trends in student interactions
    - ⚠️ Potential areas requiring intervention
    """)

    # Create two columns for the main layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Social Interaction Network with Context
        st.subheader("Student Social Interaction Network")
        st.markdown("""
        This network graph shows student interactions and their characteristics:
        - **Red nodes**: Students showing isolation patterns
        - **Yellow nodes**: Students with moderate interaction
        - **Green nodes**: Students with healthy social connections
        - **Line thickness**: Frequency of interaction
        """)
        
        # Generate sample network data
        def generate_network_data(n_students=20):
            np.random.seed(42)
            nodes = pd.DataFrame({
                'id': range(n_students),
                'name': [f'Student {i}' for i in range(n_students)],
                'risk_score': np.random.uniform(0, 1, n_students)
            })
            
            # Generate connections
            edges = []
            for i in range(n_students):
                for j in range(i+1, n_students):
                    if np.random.random() < 0.2:  # 20% chance of connection
                        weight = np.random.uniform(0.1, 1.0)
                        edges.append((i, j, weight))
            
            return nodes, edges
        
        nodes, edges = generate_network_data()
        
        # Create network visualization using plotly
        edge_x = []
        edge_y = []
        for edge in edges:
            x0, y0 = np.random.normal(0, 1, 2)  # Position for first node
            x1, y1 = np.random.normal(0, 1, 2)  # Position for second node
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')

        node_x = [np.random.normal(0, 1) for _ in range(len(nodes))]
        node_y = [np.random.normal(0, 1) for _ in range(len(nodes))]
        
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='RdYlBu_r',
                size=20,
                color=nodes['risk_score'],
                colorbar=dict(
                    title='Risk Score',
                    thickness=15,
                    xanchor='left',
                    titleside='right'
                )
            ),
            text=nodes['name'],
            textposition="top center"
        )

        fig = go.Figure(data=[edge_trace, node_trace],
                     layout=go.Layout(
                         showlegend=False,
                         hovermode='closest',
                         margin=dict(b=20,l=5,r=5,t=40),
                         xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                         yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                     ))
        
        st.plotly_chart(fig, use_container_width=True)

        # Add insights below the network
        st.info("""
        **Key Network Insights:**
        - 3 students showing increased isolation (red nodes)
        - 2 potential conflict clusters identified
        - 85% of students maintain healthy interaction patterns
        """)

    with col2:
        # Risk Factor Analysis
        st.subheader("Risk Factor Analysis")
        st.markdown("Real-time monitoring of key behavioral indicators")
        
        # Generate sample risk factors
        risk_factors = {
            "Social Isolation": 0.75,
            "Aggressive Behavior": 0.45,
            "Attendance Issues": 0.30,
            "Academic Decline": 0.60,
            "Peer Conflicts": 0.55
        }
        
        # Create gauge charts for each risk factor
        for factor, value in risk_factors.items():
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=value * 100,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': factor},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 33], 'color': "lightgreen"},
                        {'range': [33, 66], 'color': "yellow"},
                        {'range': [66, 100], 'color': "salmon"}
                    ]
                }
            ))
            fig.update_layout(height=150, margin=dict(l=10, r=10, t=30, b=10))
            st.plotly_chart(fig, use_container_width=True)

    # Behavioral Timeline
    st.subheader("Behavioral Pattern Timeline")
    st.markdown("""
    Track changes in behavioral patterns over time. This helps identify:
    - Sudden changes in social dynamics
    - Seasonal patterns in behavior
    - Effectiveness of interventions
    """)
    
    # Generate sample timeline data
    def generate_timeline_data(days=30):
        start_date = datetime.now() - timedelta(days=days)
        dates = [start_date + timedelta(days=x) for x in range(days)]
        
        data = pd.DataFrame({
            'Date': dates,
            'Isolation Events': np.random.randint(0, 5, days),
            'Aggressive Incidents': np.random.randint(0, 3, days),
            'Positive Interactions': np.random.randint(3, 10, days)
        })
        return data

    timeline_data = generate_timeline_data()
    
    fig = px.line(timeline_data, x='Date', 
                  y=['Isolation Events', 'Aggressive Incidents', 'Positive Interactions'],
                  title='30-Day Behavioral Trend Analysis')
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

    # Pattern Detection Settings
    st.subheader("Pattern Detection Settings")
    st.markdown("Customize the sensitivity of the behavioral pattern detection system")
    
    cols = st.columns(3)
    with cols[0]:
        isolation_threshold = st.number_input("Isolation Threshold", 0, 10, 3,
            help="Number of days with minimal social interaction to trigger an alert")
    with cols[1]:
        aggression_threshold = st.number_input("Aggression Threshold", 0, 10, 2,
            help="Severity level of detected aggressive behavior to trigger an alert")
    with cols[2]:
        monitoring_period = st.number_input("Monitoring Period (Days)", 1, 90, 30,
            help="Number of days to analyze for pattern detection")

    # Action buttons with clear purpose
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Update Pattern Analysis", type="primary"):
            st.success("Pattern analysis updated successfully!")
    with col2:
        if st.button("Generate Detailed Report", type="secondary"):
            generate_random_report()

    # Add new dynamic update section
    with st.expander("Generate Dynamic Analysis Report"):
        st.subheader("Analysis Parameters")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            isolation_threshold = st.slider(
                "Isolation Threshold", 
                min_value=0, 
                max_value=100, 
                value=65,
                help="Alert threshold for social isolation patterns"
            )
        
        with col2:
            aggression_threshold = st.slider(
                "Aggression Threshold", 
                min_value=0, 
                max_value=100, 
                value=75,
                help="Alert threshold for aggressive behavior"
            )
        
        with col3:
            monitoring_days = st.slider(
                "Monitoring Period (Days)", 
                min_value=7, 
                max_value=30, 
                value=14,
                help="Number of days to analyze patterns"
            )

        # Update button for dynamic analysis
        if st.button("Generate Analysis Report", type="primary"):
            with st.spinner("Analyzing patterns..."):
                time.sleep(0.5)
                
                # Generate random data based on user inputs
                dates = pd.date_range(end=datetime.now(), periods=monitoring_days)
                
                isolation_data = np.random.normal(
                    loc=isolation_threshold * 0.8, 
                    scale=15, 
                    size=monitoring_days
                ).clip(0, 100)
                
                aggression_data = np.random.normal(
                    loc=aggression_threshold * 0.7, 
                    scale=12, 
                    size=monitoring_days
                ).clip(0, 100)

                # Current values
                current_isolation = isolation_data[-1]
                current_aggression = aggression_data[-1]
                risk_score = (current_isolation * 0.5 + current_aggression * 0.5)
                
                # Display dynamic report
                st.success("Analysis complete!")
                
                st.markdown(f"""
                ### Dynamic Analysis Report
                
                #### Risk Assessment
                - Isolation Index: {current_isolation:.1f}%
                - Aggression Index: {current_aggression:.1f}%
                - Combined Risk Score: {risk_score:.1f}%
                
                #### Key Findings
                {generate_findings(current_isolation, current_aggression, isolation_threshold, aggression_threshold)}
                
                #### Recommendations
                {generate_recommendations(risk_score)}
                """)

                # Show trend chart
                df = pd.DataFrame({
                    'Date': dates,
                    'Isolation Index': isolation_data,
                    'Aggression Index': aggression_data
                })
                
                fig = px.line(df, x='Date', y=['Isolation Index', 'Aggression Index'],
                             title='Behavioral Trends Analysis')
                st.plotly_chart(fig, use_container_width=True)

def generate_findings(isolation, aggression, iso_threshold, agg_threshold):
    findings = []
    if isolation > iso_threshold:
        findings.append(f"⚠️ Isolation levels ({isolation:.1f}%) exceed threshold ({iso_threshold}%)")
    if aggression > agg_threshold:
        findings.append(f"🚨 Aggression levels ({aggression:.1f}%) exceed threshold ({agg_threshold}%)")
    if not findings:
        findings.append("✅ All metrics within normal ranges")
    return "\n".join([f"- {finding}" for finding in findings])

def generate_recommendations(risk_score):
    if risk_score > 75:
        recs = [
            "Immediate intervention required",
            "Schedule urgent assessment",
            "Increase monitoring frequency"
        ]
    elif risk_score > 50:
        recs = [
            "Regular check-ins recommended",
            "Review support system effectiveness",
            "Monitor for escalation patterns"
        ]
    else:
        recs = [
            "Maintain current monitoring level",
            "Continue positive reinforcement",
            "Document progress patterns"
        ]
    return "\n".join([f"- {rec}" for rec in recs])

def create_gauge_chart(title, value):
    """Creates a gauge chart for risk factors"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        title = {'text': title},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 20], 'color': "lightgreen"},
                {'range': [20, 50], 'color': "yellow"},
                {'range': [50, 100], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': value
            }
        }
    ))
    fig.update_layout(height=200)
    st.plotly_chart(fig, use_container_width=True)

def generate_detailed_analysis(risk_score, current_isolation, current_aggression, monitoring_days):
    """Generate detailed risk analysis with rich formatting and icons"""
    
    # Risk categories with icons
    risk_categories = {
        "Critical": "🔴",
        "High": "🟠",
        "Moderate": "🟡",
        "Low": "🟢"
    }
    
    # Determine overall risk level
    if risk_score > 85: risk_level = "Critical"
    elif risk_score > 70: risk_level = "High"
    elif risk_score > 50: risk_level = "Moderate" 
    else: risk_level = "Low"

    # Generate behavioral indicators
    indicators = []
    if current_isolation > 80:
        indicators.append("🚨 Severe social withdrawal detected")
    elif current_isolation > 60:
        indicators.append("⚠️ Increased isolation patterns")
    
    if current_aggression > 80:
        indicators.append("⛔ Critical aggression risk")
    elif current_aggression > 60:
        indicators.append("⚠️ Elevated aggression indicators")

    # Generate intervention urgency
    if risk_score > 85:
        urgency = "🚨 **IMMEDIATE INTERVENTION REQUIRED**"
    elif risk_score > 70:
        urgency = "⚠️ **Urgent Attention Needed**"
    elif risk_score > 50:
        urgency = "📊 Enhanced Monitoring Recommended"
    else:
        urgency = "✅ Continue Standard Monitoring"

    return risk_level, risk_categories[risk_level], indicators, urgency

def generate_support_recommendations(risk_score, isolation_trend, aggression_trend):
    """Generate targeted support recommendations based on risk factors"""
    
    recommendations = []
    
    # Core recommendations based on risk level
    if risk_score > 85:
        recommendations.extend([
            "🏥 Initiate crisis intervention protocol",
            "👥 Schedule immediate clinical assessment",
            "📞 Alert emergency response team",
            "🔔 Increase monitoring frequency to hourly checks"
        ])
    elif risk_score > 70:
        recommendations.extend([
            "📋 Conduct comprehensive risk assessment",
            "👥 Schedule urgent counseling session",
            "📱 Implement daily check-in protocol",
            "📊 Review and adjust safety plan"
        ])
    
    # Additional recommendations based on specific patterns
    if isolation_trend == "increasing":
        recommendations.extend([
            "🤝 Enhance social support network engagement",
            "📅 Schedule structured social activities",
            "👥 Implement peer support program"
        ])
    
    if aggression_trend == "increasing":
        recommendations.extend([
            "🧘 Implement de-escalation techniques",
            "😤 Review anger management strategies",
            "🎯 Identify and document triggers"
        ])
    
    return recommendations

if __name__ == "__main__":
    show_behavioral_patterns()