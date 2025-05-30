from bokeh.models import ColumnDataSource, NumeralTickFormatter, HoverTool
from bokeh.plotting import figure
from bokeh.embed import components
from django.db.models import Max, Min
from django.shortcuts import render
import math
from gdp.models import GDP


# Create your views here.
def index(request):
    # define the year for which we need data
    max_year = GDP.objects.aggregate(max_yr=Max('year'))['max_yr']
    min_year = GDP.objects.aggregate(min_yr=Min('year'))['min_yr']
    year = request.GET.get('year', max_year)

    # define number of countries to fetch
    count = int(request.GET.get('count', 10))

    gdps = GDP.objects.filter(year=year).order_by('gdp').reverse()[:count]

    country_names = [d.country for d in gdps]
    country_gdps = [d.gdp for d in gdps]

    cds = ColumnDataSource(data=dict(country_names=country_names, country_gdps=country_gdps))

    fig = figure(x_range=country_names, height=500, width=800, title=f'Top {count} GDPs ({year})',)
    fig.title.align = 'center'
    fig.title.text_font_size = '1.5em'
    fig.yaxis[0].formatter = NumeralTickFormatter(format='$0.0a')
    fig.xaxis.major_label_orientation = math.pi / 4

    fig.vbar(source=cds, x='country_names', top='country_gdps', width=0.8)
    tooltips = [
        ('country_name', '@country_names'),
        ('GDP', '@country_gdps{,}'),
    ]
    fig.add_tools(HoverTool(tooltips=tooltips))

    script, div = components(fig)

    context = {
        'script': script,
        'div': div,
        'years': range(min_year, max_year + 1),
        'count': count,
        'year_selected': year,
    }

    if request.htmx:
        return render(request, 'partials/gdp-bar.html', context)

    return render(request, 'index.html', context)


def line(request):
    countries = GDP.objects.values_list('country', flat=True).distinct()
    country = request.GET.get('country', 'Germany')

    gdps = GDP.objects.filter(country=country).order_by('year')

    # Multiline chart
    year_data = []
    gdp_data = []
    co = ['Germany', 'China', 'France']

    for count in co:
        co_gdps = GDP.objects.filter(country=count).order_by('year')
        ml_country_years = year_data.append([d.year for d in co_gdps])
        ml_country_gdps = gdp_data.append([d.gdp for d in co_gdps])

    # End of Multiline

    country_years = [d.year for d in gdps]
    country_gdps = [d.gdp for d in gdps]

    cds = ColumnDataSource(data=dict(country_years=country_years, country_gdps=country_gdps))

    # Multiline

    cds_ml = ColumnDataSource(data=dict(
        country_years=year_data,
        country_gdps=gdp_data,
        names=co,
        colors=['red', 'green', 'blue'],
    ))

    # end of Multiline

    fig = figure(height=500, title=f'{country} GDP')
    fig.title.align = 'center'
    fig.title.text_font_size = '1.5em'
    fig.yaxis[0].formatter = NumeralTickFormatter(format='$0.0a')

    fig.line(
        source=cds,
        x='country_years',
        y='country_gdps',
        line_width=2,
    )

    # Multiline

    fig2 = figure(height=500, title=f'Multiline GDP')
    fig2.title.align = 'center'
    fig2.title.text_font_size = '1.5em'
    fig2.yaxis[0].formatter = NumeralTickFormatter(format='$0.0a')

    fig2.multi_line(
        source=cds_ml,
        xs='country_years',
        ys='country_gdps',
        line_width=2,
        legend_group='names',
        line_color='colors'
    )
    fig2.legend.location = "top_left"

    script1, div1 = components(fig2)
    # end of multiline

    tooltips = [
        ('country_year', '@country_years'),
        ('GDP', '@country_gdps{,}'),
    ]

    fig.add_tools(HoverTool(tooltips=tooltips))

    script, div = components(fig)

    context = {
        'countries': countries,
        'country': country,
        'script': script,
        'div': div,
        'div1': div1,
        'script1': script1,
    }

    if request.htmx:
        return render(request, 'partials/gdp-bar.html', context)

    return render(request, 'line.html', context)