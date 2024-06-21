import plotly.graph_objects as go

def generate_response(agent, memory, user_input, user):
    # Logic to generate response using the agent and memory
    return agent.run(user_input)

def create_visualization(data, data_type):
    if data_type == "air_quality":
        fig = go.Figure(data=go.Scatter(x=data['dates'], y=data['aqi'], mode='lines'))
        fig.update_layout(title="Air Quality Index Over Time", xaxis_title="Date", yaxis_title="AQI")
    elif data_type == "climate":
        fig = go.Figure(data=go.Bar(x=data['years'], y=data['temperatures']))
        fig.update_layout(title="Average Temperature by Year", xaxis_title="Year", yaxis_title="Temperature (°C)")
    elif data_type == "biodiversity":
        fig = go.Figure(data=go.Pie(labels=data['species'], values=data['counts']))
        fig.update_layout(title="Species Distribution")
    else:
        return None
    
    return fig.to_json()
