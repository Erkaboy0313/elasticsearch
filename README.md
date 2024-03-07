# Django Project with Docker Setup

This Django project is configured to run using Docker containers. Follow the instructions below to set up and run the project successfully.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3. Create a `.env` file in the root directory of the project and define the following environment variables:

    ```plaintext
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```

## Running the Project with Docker

1. Build and start the Docker containers:

    ```bash
    docker-compose up --build
    ```

2. Enter the Elasticsearch container to set up authentication credentials:

    ```bash
    docker-compose exec elasticsearch bash
    ```

3. Inside the Elasticsearch container, execute the following command to add a user and password:

    ```bash
    ./bin/elasticsearch-users useradd admin -p 123456 -r superuser
    ```

    Note: Replace `admin` and `123456` with your desired username and password specified in the settings file.

4. Exit the Elasticsearch container and enter the Django container:

    ```bash
    docker-compose exec web sh
    ```

5. Rebuild the search indexes:

    ```bash
    python manage.py search_index --rebuild
    ```

6. Once the setup is complete, the project should be accessible at:

    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Adding or Updating Products

To add or update a product, navigate to the following URL:

[http://127.0.0.1:8000/api/v1/product/](http://127.0.0.1:8000/api/v1/product/)

## Searching for Products

To search for products, use the following URL format:

[http://127.0.0.1:8000/api/v1/product-search/?search=YourSearchQuery](http://127.0.0.1:8000/api/v1/product-search/?search=YourSearchQuery)

Replace `YourSearchQuery` with the name or product ID you want to search for.

## Running Without Docker

If you prefer to run the project without Docker, make sure Elasticsearch is installed and running on your local machine. You can install Elasticsearch by visiting [Elasticsearch Installation Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html).

Once Elasticsearch is installed and running locally, you can follow the standard Django project setup and configuration process. Ensure you have the necessary Python packages installed and update the Django settings accordingly.
