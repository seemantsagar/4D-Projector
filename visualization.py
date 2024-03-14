import plotly.graph_objs as go

def plot_4d_projection(projection, edges=None):
    """
    Plot the 4D projection of a 3D object in a 3D plane using Plotly.
    """
    # Create a 3D scatter plot for the vertices
    trace_vertices = go.Scatter3d(
        x=projection[:, 0],
        y=projection[:, 1],
        z=projection[:, 2],
        mode='markers',
        marker=dict(
            size=5,
            color='red',
            opacity=0.8
        )
    )

    # If edges are provided, create a 3D line plot for the edges
    if edges is not None:
        trace_edges = go.Scatter3d(
            x=edges[:, 0],
            y=edges[:, 1],
            z=edges[:, 2],
            mode='lines',
            line=dict(
                color='black',
                width=2
            )
        )
        data = [trace_vertices, trace_edges]
    else:
        data = [trace_vertices]

    layout = go.Layout(
        scene=dict(
            xaxis=dict(title='X'),
            yaxis=dict(title='Y'),
            zaxis=dict(title='Z'),
            aspectratio=dict(x=1, y=1, z=1)
        )
    )

    fig = go.Figure(data=data, layout=layout)
    fig.show()