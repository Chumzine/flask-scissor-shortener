# flask-scissor-shortener

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][twitter-shield]][twitter-url]


<h3 align="center">Scissor</h3>

  <p align="center">
    A URL shortening and QR Code generating website built with Flask
    <br />
    <a href="https://github.com/Chumzine/flask-scissor-shortener"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Chumzine/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/Chumzine/repo_name/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About Scissor</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#what-i-learnt">What I Learnt</a></li>
    <li>
      <a href="#how-to-use">How to Use</a>
      ul>
        <li><a href="#sample">Sample Screenshots</a></li>
      </ul>
    </li>
    <li>
      <a href="#cloning-this-project">Cloning This Project</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About Scissor

**Scissor** is a simple tool that makes URLs as short as possible. "Brief is the new black", is the inspiration behind **Scissor**. It allows users paste a long URL and get a short URL generated automatically, which makes for easy sharing on social media platforms or any other channel.
Customisation of shortened URLs is another feature of **Scissor**. Users can choose their own custom domain name and customize the URL to reflect their brand or content. Also, users get to generate QR Codes for their shortened URLs and download it. Tracking of the shortened URL and the history of the links created by users is also implemented in **Scissor**.

**Scissor** was built by <a href="https://github.com/Chumzine/">Adaobi Chuma-Okeke</a>, with knowledge from the Backend Engineering live classes for Python by <a href="https://thealtschool.com/">AltSchool Africa</a> as well as through thorough research.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Features

* URL shortening
* Customising of shortened URL
* QR Code generation
* URL history
* Analytics



### Built With

* ![Python][python]
* ![Flask][flask]
* ![SQLite][sqlite]
* ![HTML5][html5]
* ![CSS3][css3]
* ![Jinja][jinja]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- What I Learnt from Building this Blog -->
## What I Learnt

Working on this project was amazing. I got to learn a lot of new concepts and implement them as well as brush up on what I already knew in the following areas:
* Python
* Flask
* Materialize CSS
* Routing
* Database Management
* Debugging
* Authentication
* Authorization
* Web Development
* Deployment with Heroku
* Internet security

<p align="right"><a href="#readme-top">back to top</a></p>




<!-- HOW TO USE -->
## How to Use

To run this application, follow these steps:

1. Open this link on your browser, https://scissad.me/ or https://scissor-flask-app.onrender.com/ 
   
2. Create a user account or log in if you already have an account;
   *To create an account: Click on 'Register' in the side navigation bar to open up a registration form*
   *To log in: Click on 'Login' in the side navigation bar to open up the login form*
   
3. Once authenticated, the 'Create' button will appear on the top navigation bar. Click it to either create your shortened URL or generate your QR Code.
   
4. Fill in the required fields to create what you want.
   *For the QR Code generation, you can download your QR Code image once generated*
   
6. Click on 'Analytics' in the side navigation bar to see your links history and track the number of clicks on your shortened URL.
 
7. You may now log out using the 'Logout' option in the side navigation bar.



## Sample Screenshots
![2023-06-28](https://github.com/Chumzine/flask-scissor-shortener/assets/86481843/5ff32f53-6cd0-45e0-bb97-176377f456fe)

![Screenshot 2023-07-09 203505](https://github.com/Chumzine/flask-scissor-shortener/assets/86481843/4e294083-72be-4adc-8192-95d7c6e2d161)

![Screenshot 2023-07-09 203525](https://github.com/Chumzine/flask-scissor-shortener/assets/86481843/52223bc9-7242-451f-9dab-0b30f5df5753)

![Screenshot 2023-07-09 203557](https://github.com/Chumzine/flask-scissor-shortener/assets/86481843/abe97e67-2b96-45b9-9c55-bb89bf685263)

![Screenshot 2023-07-09 205048](https://github.com/Chumzine/flask-scissor-shortener/assets/86481843/c620da4c-6d77-4de1-a071-9a8c7fb4bcee)



<p align="right"><a href="#readme-top">back to top</a></p>




<!-- CLONING THIS PROJECT -->
## Cloning This Project

To get a local copy up and running follow these steps.

### Prerequisites

Python3: [Get Python](https://www.python.org/downloads/)

Text Editor/Integrated Development Environment(IDE)

### Installation

1. Clone this repo
   ```sh
   git clone https://github.com/Chumzine/flask-scissor-shortener.git
   ```
2. Activate the virtual environment
   
   *For Windows*
   ```sh
   env\Scripts\activate
   ```
   *For Linux/Mac*
   ```sh
   env\bin\activate
   ```
4. Install project packages
   ```sh
   pip install -r requirements.txt
   ```
5. Run the code
   ```sh
   python main.py
   ```
6. Open the link generated in the terminal on a browser

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## License

Distributed under the MIT License. See <a href="https://github.com/Chumzine/flask-scissor-shortener/blob/main/LICENSE">LICENSE</a> for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Adaobi Chuma-Okeke - [@twitter_handle](https://twitter.com/chumzine) - chumzine@gmail.com

Project Link: [https://github.com/Chumzine/flask-scissor-shortener](https://github.com/Chumzine/flask-scissor-shortener)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [AltSchool Africa School of Engineering](https://altschoolafrica.com/schools/engineering)
* [Caleb Emelike's Python, Flask and Database Lessons](https://github.com/CalebEmelike)
* [Python Tutorial – How to Create a URL Shortener using Flask by freeCodeCamp](https://www.freecodecamp.org/news/python-tutorial-how-to-create-a-url-shortener-using-flask/)
* [YouTube](https://www.youtube.com)
* [Adeniyi Olanrewaju Mark](https://github.com/engrmarkk)
* [Stack Overflow](https://stackoverflow.com/)
* [Google](https://google.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Chumzine/flask-scissor-shortener.svg?style=for-the-badge
[contributors-url]: https://github.com/Chumzine/flask-scissor-shortener/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Chumzine/flask-scissor-shortener.svg?style=for-the-badge
[forks-url]: https://github.com/Chumzine/flask-scissor-shortener/network/members
[stars-shield]: https://img.shields.io/github/stars/Chumzine/flask-scissor-shortener.svg?style=for-the-badge
[stars-url]: https://github.com/Chumzine/flask-scissor-shortener/stargazers
[issues-shield]: https://img.shields.io/github/issues/Chumzine/flask-scissor-shortener.svg?style=for-the-badge
[issues-url]: https://github.com/Chumzine/flask-scissor-shortener/issues
[license-shield]: https://img.shields.io/github/license/Chumzine/flask-scissor-shortener.svg?style=for-the-badge
[license-url]: https://github.com/Chumzine/flask-scissor-shortener/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/she-adaobi-chuma-okeke-3677a9140
[twitter-shield]: https://img.shields.io/badge/-@chumzine-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/chumzine
[twitter-url]: https://twitter.com/chumzine
[jinja]: https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black
[html5]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[css3]: https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[sqlite]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
