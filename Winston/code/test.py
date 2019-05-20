for i in range(0,21):
    fn = "https://raw.githubusercontent.com/wel51x/ItsOver9000-DS/master/charts/chart" + str(i) + ".png"
    fn_out = "chart"  + str(i)
    layout = go.Layout(
        xaxis = go.layout.XAxis(
            visible = False,
            range = [0, img_width*scale_factor]),
        yaxis = go.layout.YAxis(
            visible=False,
            range = [0, img_height*scale_factor],
            # the scaleanchor attribute ensures that the aspect ratio stays constant
            scaleanchor = 'x'),
        width = img_width*scale_factor,
        height = img_height*scale_factor,
        margin = {'l': 0, 'r': 0, 't': 0, 'b': 0},
        images = [go.layout.Image(
            x=0,
            sizex=img_width*scale_factor,
            y=img_height*scale_factor,
            sizey=img_height*scale_factor,
            xref="x",
            yref="y",
            opacity=1.0,
            layer="below",
            sizing="stretch",
            source=fn)]
    )
    # we add a scatter trace with data points in opposite corners to give the Autoscale feature a reference point
    fig = go.Figure(data=[{
        'x': [0, img_width*scale_factor],
        'y': [0, img_height*scale_factor],
        'mode': 'markers',
        'marker': {'opacity': 0}}],layout = layout)
    py.iplot(fig, filename=fn_out)
