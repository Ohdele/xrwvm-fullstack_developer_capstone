

# FULL STACK APPLICATION DEVELOPMENT CAPSTONE PROJECT OVERVIEW

I am tasked with building a website for a national car dealership to allow customers to access and submit reviews for dealership branches across the U.S. The platform includes features for anonymous, authorized, and admin users.


# Use Cases

## Anonymous Users:
- View About Us, Contact Us, and dealership list pages.
- Filter dealerships by state and view details.
- View dealership reviews.

## Authorized Users:
- In addition to the above, authorized users can write reviews.
- Reviews appear at the top of the list on the dealership details page.

## Admin Users:
- Admins can log in to manage dealership data, including adding new car makes, models, and attributes.

#  Developer Role
As the Lead Full-Stack Software Developer, I followed best practices to develop this portal.

#  ARCHITECTURE OVERVIEW

## Project Breakdown:
- Fork and clone GitHub repo from IBM developer skills network
- Created static pages for user stories
- Run the Django app locally
- Implement user management (Django auth, REACT frontend)
- Implement backend services (Node.js for dealers and reviews, MongoDB, Docker)
- Deploy sentiment analyzer on Code Engine
- Create Django models, views for car model/make
- Create Django proxy services for dealers/reviews
- Add dynamic pages with Django templates (dealers, reviews, add reviews)
- Set up CI/CD, test, and deploy on Kubernetes

## Solution Architecture:
- **User Interaction**: Web browser → Django Website
- **Django App**: 
  - Microservices: get_cars/, get_dealers/, get_dealers/:state, dealer/:id, review/dealer/:id, add_review/
  - Uses SQLite for Car Make and Car Model data.
  
- **Dealerships and Reviews Service**: Express-Mongo service in Docker:
  - Microservices: /fetchDealers, /fetchDealer/:id, fetchReviews, fetchReview/dealer/:id, /insertReview

- **Sentiment Analyzer**: IBM Cloud Code Engine:
  - Microservice: /analyze/:text for sentiment analysis


# Task 1: Application - Static Pages

1. **Fork the GitHub Repo**: Fork the provided repository containing the project template.

2. **Clone Repository**: Clone the forked repository to your local environment.

3. **Run Django App**: Set up the local development environment and run the Django application to verify that the app skeleton is working correctly.

4. **Add Navigation**: Integrate Bootstrap's navigation component into the project to improve user experience and page navigation across the website.

5. **Add Static Pages**:
   - Create the "About Us" page to provide basic information about the car dealership.
   - Create the "Contact Us" page to enable users to reach out for support or inquiries.

### Conclusion:
I prepared the GitHub repository and cloned the app skeleton to start building the dealer review app. As a warm-up task, I created several static pages, including "About Us" and "Contact Us", to test the app structure. These static pages serve as the foundational elements for user interaction before diving into more complex features and dynamic content. I then pushed the changes made into the GitHub repository. 

Next, is some actual design and development work.


# TASK 2: User Management Overview

In this task, I implemented a user management system to allow administrators to manage users based on roles such as anonymous and registered users. The goal is to add the core functionality of registration, login, and logout for proper user authentication and authorization.

1. **Create Superuser**: 
   - Set up a Django superuser to allow admin-level access for managing users.
   - Used the `python manage.py createsuperuser` command to create the superuser.

2. **Build Client-Side Interface**: 
   - Designed and configured the client-side UI to allow users to register, log in, and log out.
   - Integrated with Django’s built-in authentication views.

3. **Check Client Configuration**: 
   - Verified that all client-side forms and buttons, such as the register button, login button, and logout button, were correctly wired to their respective Django views.

4. **Add Login View**: 
   - Implemented the login functionality with Django’s authentication system.
   - Ensured that users could log in securely and be redirected to their desired page after logging in.

5. **Add Logout View**: 
   - Implemented the logout functionality to handle user sessions and ensure users could safely log out of the platform.

6. **Add Registration View**: 
   - Created a user registration view to handle new user sign-ups.
   - The registration process included basic user information, with proper validations for input fields.

## Summary:
This task focused on implementing a robust user management system within the Django app, enabling user registration, login, and logout. I ensured that only authorized users could access certain parts of the platform based on their role. By using Django’s built-in authentication features, I streamlined the process of managing users effectively.

## Conclusion:
I successfully added user management-related templates and views to the app, enabling user authentication and role-based access control. In the next task, I will focus on creating car/make-related models, templates, and views to handle the dealership data.


# TASK 3: Mongo DB Dockerized Server Overview

In the previous task, I implemented user authentication using the Django framework and React. For this task, the focus shifts to building the backend services for the application, which will be responsible for communicating with MongoDB.

The backend services will be built using Node.js with an Express framework. These services will expose RESTful API endpoints that the Django application will interact with. The entire application, including the backend services, will be containerized using Docker and deployed on IBM Cloud Code Engine.


1. **Node.js Application**:
   - Set up a containerized Node.js application that connects to MongoDB to manage the data for the dealership reviews and dealer information.

2. **Express API Endpoints**:
   - Implement the following API endpoints to fetch necessary data:
     - `/fetchReviews/dealer/{dealer_id}`: Fetch reviews for a specific dealer.
     - `/fetchDealers`: Fetch a list of all dealers.
     - `/fetchDealer/{dealer_id}`: Fetch detailed information for a specific dealer.
     - `/fetchDealers/{state}`: Fetch dealers based on a specific state (e.g., Kansas).

3. **Dockerize the App**:
   - Containerize the Node.js application with Docker, allowing for a portable and consistent environment for development, testing, and deployment.

## Summary:
In this task, I developed a Dockerized Node.js application that communicates with MongoDB and exposes several API endpoints for fetching dealer and review data. These services will provide the necessary backend functionality for the Django application to integrate and display the data.

## Conclusion:
In this task, I successfully created a containerized Node.js application that uses MongoDB as its backend. This app exposes various API endpoints which the Django application can use to fetch dealer and review data.

  Django Models and Views

1. **Create Car Models**:  
   - Implemented `CarModel` and `CarMake` Django models to represent the car inventory.  
   - These models store details such as car make, model, year, and dealer ID.  
   - Registered the models with the Django admin site to allow for CRUD operations.

2. **Add Data**:  
   - Populated the `CarModel` and `CarMake` models with initial data. Created car objects associated with different dealerships.

3. **Proxy Services**:  
   - Developed Django views to integrate external data, such as dealer and review information, into the application.  
   - These views act as proxy services that fetch data from the Node.js backend (via the previously defined API endpoints) and render the data on the frontend.

## Summary:
In this module, I implemented `CarModel` and `CarMake` models in Django to represent car inventory. Additionally, I created proxy services in Django to interact with the external backend API endpoints (built with Node.js and MongoDB). These services fetch and display dealer and review data on the front-end via Django templates.


Build CarModel and CarMake Django Models

A dealership typically manages cars from one or more makers or manufacturers, and customers should be allowed to review the cars they purchased from a dealer.

The goal of this task was to build models that represent car makes and models in the Django application, enabling us to manage a dealership's inventory.

- The `CarModel` stores information such as the car's make, model, year, and associated dealer.
- The `CarMake` model stores details about different car makes, such as their name and description.

### Steps:
- I created these two models within Django and linked them with the car dealer information.
- Registered both models with the Django admin interface to easily manage and perform CRUD operations.

Create Django Proxy Services for Backend APIs

Previously, I created `CarModel` and `CarMake` Django models, storing data in an SQLite database. The backend APIs for dealing with dealers and reviews, however, reside in a MongoDB database, served through the Node.js application.

### Objective:
To integrate this external dealer and review data into the Django app, I created proxy services in Django. These services fetch the required data by calling the API endpoints exposed by the Node.js application.

### Steps:
- I implemented Django views as proxy services that send HTTP requests to the Node.js backend API.
- The data returned from the backend (in JSON format) is processed within the Django views and converted into Python objects such as `CarDealer` and `DealerReview`.
- The processed data is then returned as an HTTP response and rendered on the frontend.

## Conclusion:
In this task, I learned how to create proxy services within Django to interact with external cloud functions. I was able to call APIs, convert the JSON responses into Python objects, and send the data back to the user in a structured format. The next step will be to create Django templates to display these objects on the frontend.


# Task 4: Dynamic Pages

In the previous TASK, I created the necessary backend services to manage dealerships and reviews.

NEXT, I created a user-friendly and aesthetic front-end pages to present these services to end users.

### Prerequisites:  
- **Sentiment Analyzer**: Ensure the sentiment analysis service is deployed on IBM Code Engine and accessible via API. 
- Backend service with Express-MongoDB from the previous task should be running and accessible on one of the terminals. 

1. **Create Dealers Component**:  
   - Develop a React component that fetches and displays a list of all dealerships using the backend API (`/fetchDealers`).  
   - Include sorting and filtering options for better usability, such as filtering dealerships by state.  
   - Ensure error handling and loading indicators are in place for API calls.

2. **Dealer Details Component**:  
   - Build a React component to display detailed reviews for a selected dealer.  
   - Fetch reviews using the API endpoint (`/fetchReviews/dealer/{dealer_id}`).  
   - Integrate the sentiment analyzer API (`/analyze/{text}`) to analyze and display the sentiment of each review.  
   - Implement pagination for reviews if the number is large.

3. **Review Submission Page**:  
   - Create a dedicated page for authorized users to submit reviews for specific dealerships.  
   - Fetch dealership details for context and prefill relevant fields.  
   - Ensure validation for user input, such as rating (e.g., 1-5 stars) and review text.  
   - Submit the review to the backend using the API endpoint (`/insertReview`).

## Summary:  
In this module, I developed dynamic React pages to:  
1. Display a list of dealerships with sorting and filtering options.  
2. Show detailed reviews for a selected dealer, with sentiment analysis integration.  
3. Enable authorized users to submit reviews for dealerships through a user-friendly form.

CONCLUSION:
In this lab, I created a dealer list, dealer details, and a provision for adding reviews. At this point, I have completed the main app development work.

The next steps will involve fine-tuning, testing, and deployment.


# Task 5: CI/CD

## CI/CD Workflow Setup

1. **Understand GitHub Workflow Template**:
   - Review the pre-configured GitHub workflow for CI/CD included in the project repository.
   - Identify steps for build, test, and deployment automation.

2. **Configure Linting Jobs**:
   - Set up linting for Python using `flake8` and JavaScript using `JSHint` to maintain code quality.
   - Ensure linting checks are included in the workflow.

3. **Enable GitHub Actions**:
   - Activate GitHub Actions in the repository settings and run the Linting workflow to ensure the code adheres to the defined standards.
   - Test the CI/CD pipeline by triggering the linting workflow on code pushes or pull requests.

## Summary:
This module establishes a CI/CD pipeline using GitHub Actions. It includes setting up automated linting to maintain code quality for Python and JavaScript files, ensuring a seamless development workflow.


CI/CD Setup

1. **Enable GitHub Actions**:
   - Integrate GitHub Actions to automate workflows triggered by events like code pushes or pull requests.

2. **Set Up Linting Services**:
   - Configure linting for Python (flake8) to identify potential code issues and adhere to PEP 8 standards.
   - Configure linting for JavaScript (JSHint) to enforce coding standards.

3. **Define Workflow Configuration**:
   - Create a YAML workflow file to automate linting jobs.
   - Configure the workflow to run on specific branches, ensuring team-wide code quality compliance.

## Summary:
The CI/CD setup automates essential tasks like linting using GitHub Actions, improving development efficiency and code maintainability.


Containerize & Deploy to Kubernetes

MY Django application is fully functional, and MY team is happy. However, THERE IS a new request. The company is looking at using containers to manage and deploy the application. Furthermore, the management is interested in using the hybrid cloud strategy, where some applications and services reside on a private cloud and others on a public cloud. To provide a more robust development experience, I AM asked to look at Kubernetes. So, I WILL containerize the application.

## Containerize Your Application

1. **Prepare Dockerfile**:
   - Write a `Dockerfile` to package the Django application along with its dependencies.
   - Use multi-stage builds to optimize the image size.

2. **Build and Tag Image**:
   - Build the container image using Docker.
   - Tag the image with a meaningful version number.

3. **Push to Container Registry**:
   - Push the image to a container registry such as Docker Hub or a private registry.

## Kubernetes Deployment

1. **Create Deployment Files**:
   - Write YAML manifests for Deployment, Service, and Ingress resources.
   - Ensure the configurations define replica sets, load balancing, and environment variables.

2. **Deploy to Kubernetes**:
   - Use `kubectl` to apply the deployment files to a Kubernetes cluster.
   - Verify pod status, services, and ingress using `kubectl get` commands.

3. **Monitor and Test**:
   - Check the deployment logs and service endpoints for errors or issues.
   - Perform end-to-end testing to ensure functionality.

## Summary:
This task focuses on containerizing the dealership application into Docker images and deploying them on Kubernetes. It ensures scalability, supports hybrid cloud strategies, and avoids vendor lock-in.

**Conclusion**:
In this module, I successfully implemented a CI/CD pipeline using GitHub Actions, added linting to ensure code quality, containerized the Django application, and deployed it on Kubernetes. These steps enhance the application’s scalability, maintainability, and deployment flexibility.
