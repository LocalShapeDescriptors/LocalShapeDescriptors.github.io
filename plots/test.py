from bokeh.models import HoverTool, ColumnDataSource
from bokeh.plotting import figure, show, save, output_file
import glob
import os
import pandas as pd
import sys

def hex_to_rgb(hc):
    hc = hc.lstrip('#')
    return tuple(
            int(hc[i:i+2], 16)
            for i in (0,2,4)
        )

def lighten_color(rgb,factor):
    return [int(255 - (255 - i) * (1 - factor)) for i in rgb]

def create_df(f=None,dir_path=None):

    if f:
        return pd.read_csv(f)

    elif dir_path:
        files = glob.glob(os.path.join(dir_path, '*.csv'))

        df = []
        for f in files:
            df.append(pd.read_csv(f))

        return pd.concat(df)

    else:
        print('Need to pass something...')

def create_plot(
        df,
        networks,
        tools,
        title,
        x_axis,
        y_axis,
        colormap,
        plot_height=600,
        plot_width=600,
        filt=None,
        mute=False):

    p = figure(
            title=title,
            plot_height=plot_height,
            plot_width=plot_width,
            tools=tools)

    def fix_axis(axis):
        if 'volume' in axis:
            axis = axis.replace('volume', 'roi') + ' (\u03BCm\u00b3)'
        axis = axis.replace('_', ' ').capitalize()
        return axis

    p.xaxis.axis_label = fix_axis(x_axis)
    p.yaxis.axis_label = fix_axis(y_axis)

    df['color'] = [colormap[x] for x in df['method']]

    kwargs = {}

    kwargs['x']=x_axis
    kwargs['y']=y_axis

    for m,c in colormap.items():

        kwargs['color']=c[0]
        kwargs['source']=df[df.method==m]
        kwargs['legend_label']=m

        fc = tuple(lighten_color(hex_to_rgb(c[0]),0.5))

        if mute:
            kwargs['muted_alpha']=0.01

        s=7

        if 'LSD' in m:
            line_dash = 'dashed'
            p.square(fill_color=fc,size=s,**kwargs)
        else:
            line_dash = []
            p.circle(fill_color=fc,size=s,**kwargs)

        p.line(line_dash=line_dash,**kwargs)

    return p

if __name__ == '__main__':

    df = create_df(dir_path=sys.argv[1])

    df = df.loc[df['has_mask'] == 1]

    cm = {
        'Baseline': ['#4E73AE','\\vanilla'],
        'Long Range': ['#8174B1', '\\longrangepadding'],
        'Malis': ['#008080', '\\malis'],
        'FFN': ['#000000', '\\ffn'],
        'MtLSD': ['#C24F54', '\\mtlsd'],
        'AcLSD': ['#58A76A', '\\aclsd'],
        'AcrLSD': ['#DB8457', '\\acrlsd']
    }

    for k,v in cm.items():
        df.method.replace(v[1], k, inplace=True)

    hover = HoverTool(
                tooltips=[
                    ("Method", "@method"),
                    ("Roi Size", "@volume_size \u03BCm\u00b3"),
                    ("Voi Sum", "@voi_sum"),
                    ("Voi Split", "@voi_split"),
                    ("Voi Merge", "@voi_merge")
                    ]
                )

    p = create_plot(
            df,
            networks=cm.keys(),
            tools=[hover, "box_zoom,pan,reset,wheel_zoom"],
            title='test',
            x_axis='volume_size',
            y_axis='voi_sum',
            colormap=cm)

    p.legend.location = "bottom_right"
    p.legend.click_policy="hide"

    show(p)
