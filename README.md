# Tailspin Toys

This repository contains the project for a 1 hour guided workshop to explore GitHub Copilot Agent Mode and related features in Visual Studio Code. The project is a website for a fictional game crowd-funding company, with a [Flask](https://flask.palletsprojects.com/en/stable/) backend using [SQLAlchemy](https://www.sqlalchemy.org/) and [Astro](https://astro.build/) frontend using [Svelte](https://svelte.dev/) for dynamic pages.

## Start the workshop

**To begin the workshop, start at [docs/README.md](./docs/README.md)**

Or, if just want to run the app...

## Launch the site

A script file has been created to launch the site. You can run it by:

```bash
./scripts/start-app.sh
```

Then navigate to the [website](http://localhost:4321) to see the site!

## Features

### Game Filtering
The site now includes filtering functionality that allows users to discover games based on their preferences:

- **Publisher Filter**: Filter games by publisher using the dropdown selection
- **Category Filter**: Filter games by category using the dropdown selection  
- **Combined Filtering**: Use both publisher and category filters simultaneously
- **Clear Filters**: Reset all filters to view all games

The filtering works by making API calls to the backend with query parameters, providing a responsive user experience.

## API Endpoints

The Flask backend provides the following RESTful API endpoints:

### Games
- `GET /api/games` - Get all games (supports filtering)
  - Query Parameters:
    - `publisher_id` (optional): Filter by publisher ID
    - `category_id` (optional): Filter by category ID
- `GET /api/games/{id}` - Get a specific game by ID

### Publishers
- `GET /api/publishers` - Get all publishers

### Categories
- `GET /api/categories` - Get all categories

### API Response Format
All API endpoints return JSON data. Games include nested publisher and category information:

```json
{
  "id": 1,
  "title": "Game Title",
  "description": "Game description",
  "publisher": {"id": 1, "name": "Publisher Name"},
  "category": {"id": 1, "name": "Category Name"},
  "starRating": 4.5
}
```

## License 

This project is licensed under the terms of the MIT open source license. Please refer to the [LICENSE](./LICENSE) for the full terms.

## Maintainers 

You can find the list of maintainers in [CODEOWNERS](./.github/CODEOWNERS).

## Support

This project is provided as-is, and may be updated over time. If you have questions, please open an issue.
