# GDP Analysis Dashboard

**Educational Project - Django + Bokeh Integration**

A Django web application built for educational purposes, demonstrating how to integrate Bokeh visualizations with Django and HTMX. This project follows the BugBytes tutorial and showcases interactive GDP data visualization with dynamic bar charts and line charts.

## Learning Objectives

This educational project demonstrates:
- **Django-Bokeh Integration**: How to embed interactive Bokeh plots in Django templates
- **HTMX Implementation**: Creating dynamic web interfaces without JavaScript frameworks
- **Data Visualization**: Building responsive charts with hover tools and formatting
- **Django ORM**: Querying and filtering data for visualization
- **Template Partials**: Using Django template partials with HTMX for seamless updates

## Features

- **Interactive Bar Charts**: Display top N countries by GDP for selected years
- **Line Charts**: Show GDP trends over time for individual countries
- **Multi-line Charts**: Compare GDP trends across multiple countries
- **Real-time Updates**: Uses HTMX for seamless chart updates without page reloads
- **Responsive Design**: Bootstrap-based UI that works on all devices

## Screenshots

![Bar Chart](https://github.com/user-attachments/assets/abfdef55-ff9a-4e8e-aae6-f567b24b57c6)
*Interactive bar chart with year and country count selectors*

![Line Chart](https://github.com/user-attachments/assets/c9390114-358d-40d4-8e33-ebef82f2cdb1)
*Line chart showing GDP trends and multi-country comparisons*

## Tech Stack

- **Backend**: Django 3.2+
- **Frontend**: HTML5, Bootstrap 4, HTMX
- **Visualization**: Bokeh 3.7.3
- **Database**: SQLite (default, easily configurable)
- **Additional**: django-extensions, django-htmx

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/gdp-analysis.git
   cd gdp-analysis
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django bokeh django-extensions django-htmx
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Load sample data**
   ```bash
   python manage.py populate
   ```
   *Note: You'll need to add your GDP data file at `data/gdp.json`*

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Visit the application**
   Open your browser to `http://127.0.0.1:8000/`

## Data Format

The application expects GDP data in JSON format with the following structure:

```json
[
  {
    "Country Name": "United States",
    "Country Code": "USA",
    "Year": 2023,
    "Value": 25462700000000
  },
  ...
]
```

Place your data file at `data/gdp.json` before running the populate command.

## Project Structure

```
gdp-analysis/
├── gdp/                    # Main Django app
│   ├── management/
│   │   └── commands/
│   │       └── populate.py # Data loading command
│   ├── templates/          # HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── line.html
│   │   └── partials/
│   ├── models.py          # GDP data model
│   ├── views.py           # Chart generation logic
│   └── urls.py
├── gdp_analysis/          # Django project settings
├── static/                # Static files (CSS, JS)
├── data/                  # Data files (add your gdp.json here)
└── manage.py
```

## Usage

### Bar Chart View
- Select year from dropdown to view GDP data for that year
- Adjust the count input to show top N countries
- Charts update automatically using HTMX

### Line Chart View
- Select a country from dropdown to view its GDP trend over time
- View multi-line comparison chart for predefined countries (Germany, China, France)

## Customization

### Adding More Countries to Multi-line Chart
Edit the `co` list in `gdp/views.py`:

```python
co = ['Germany', 'China', 'France', 'Your Country']
```

### Styling
Customize the appearance by modifying:
- `static/css/styles.css` for custom CSS
- Templates in `gdp/templates/` for HTML structure
- Chart styling in `gdp/views.py` using Bokeh parameters

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **Tutorial by BugBytes**: This project follows the BugBytes tutorial series on integrating Bokeh with Django
- **Educational Purpose**: Built specifically for learning Django-Bokeh integration patterns
- Uses Bokeh for powerful data visualization capabilities
- HTMX for seamless interactivity without complex JavaScript
- Bootstrap for responsive design

## Learning Resources

- [BugBytes YouTube Channel](https://www.youtube.com/@bugbytes3923) - Original tutorial source
- [Bokeh Documentation](https://bokeh.org/) - For advanced visualization techniques
- [Django Documentation](https://docs.djangoproject.com/) - Django framework reference
- [HTMX Documentation](https://htmx.org/) - For dynamic web interfaces

## Educational Notes

This project is ideal for developers learning:
- How to integrate data visualization libraries with Django
- Creating interactive web applications with minimal JavaScript
- Working with Django ORM for data queries
- Building responsive template partials
- Implementing real-time chart updates

## License

This project is for educational purposes. Feel free to use it for learning and experimentation.
