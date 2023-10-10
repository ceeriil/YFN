# YFN

YFN is the ultimate platform where creators like artists and bloggers converge to share, connect, and grow. At the heart of our community lies a strong belief in the power of creativity and collaboration. Our platform provides an interactive space for creators to post their blog content, share their art, and interact with a like-minded community.

With YFN, we're building bridges between creators, fostering connections that inspire and amplify the creative process. So, whether you're an artist, a writer, or an enthusiast, YFN is your space to create, connect, and thrive.

Welcome to the YFN community – where every creator's voice is heard and valued.

## Developer Guide

### How to run locally

1. Clone the repository:

   ```sh
   git clone https://github.com/ceeriil/YFN.git
   ```

2. Navigate into the YFN directory:

   ```sh
   cd YFN
   ```

3. Ensure you have Python 3 installed on your machine. If not, download and install Python 3 from the official [Python website](https://www.python.org/).

4. Create a virtual environment:

   ```sh
   python3 -m venv venv
   ```

5. Activate the virtual environment:

   - On Unix or MacOS, run:
     ```sh
     source venv/bin/activate
     ```
   - On Windows, run:
     ```sh
     .\venv\Scripts\activate
     ```

6. Install the requirements:

   ```sh
   pip3 install -r requirements.txt
   ```

7. Create a superuser account:

   ```sh
   python3 manage.py createsuperuser
   ```

8. Navigate into the `src` directory:

   ```sh
   cd src
   ```

9. Make migrations:

   ```sh
   python3 manage.py makemigrations
   ```

10. Apply migrations:

    ```sh
    python3 manage.py migrate
    ```

11. Run the development server:

    ```sh
    python3 manage.py runserver
    ```

12. Visit `http://127.0.0.1:8000/admin` to make changes to the database.

> **Note:** The project currently uses SQLite as the default database.

## Features

### Current Features

- Create an account
- Login
- Descriptive homepage
- Profile update
- Profile info page
- Add a post
- Edit a post
- Delete a post

### Fixes Needed

- Fix stylings for all the pages
- Make add post in a modal

### Features Needed

- Update models for profile info to include bio, about, website link, Instagram link, Facebook link, location
- Add search functionality
- Add comment and like functionality
- Expand post model
- Possibly use rich text editor for post

Please raise an issue for any feature that needs to be added.

## Acknowledgments

This project uses Django Project Boilerplate by justdjango. Refer to [OLDREADME.md](docs/OLDREADME.md) to view the template README.
