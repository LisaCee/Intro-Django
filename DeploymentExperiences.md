heroku deploy: https://dashboard.heroku.com/apps/lambda-reviews/access
https://lambda-reviews.herokuapp.com/

heroku deploy #2: https://lambda-reviews1.herokuapp.com/
django repo: https://github.com/LisaCee/Intro-Django


- Summarize the key steps in the deployment process. 
  - What went well?
    I took time with this sprint-challenge to really read through the instructions before I tried to implement them.  I think this lead to a more smooth deploy than I would have had if I had just jumped in and started installing new dependencies.  

    I thought that my deploy worked on the first attempt, but after visiting the app I discovered some errors.  -- see challenges

  - What challenges did you face? 
    I felt really anxious going into this challenge because it has been months since I've used Heroku and never with Django or Python. 

    My first challenge was that I couldn't get my local Heroku updated.  I tried to run update, but it just got stuck in my terminal.  Then I tried to reinstall Heroku, which appeared to work but my terminal still said I have an older version.  I decided to continue without ensuring the update so that I could continue with the sprint in the given time.

    Another challenge was the lack of benchmarks that this sprint provided.  I could not make sure that everything was running correctly until I tried to deploy.  I remedied this concern by pushing to Github frequently.  

    Finally I had a hard time understanding the instructions regarding database_url.
    After struggling with it for a while, I found some helpful information at the end of the readme in the troubleshooting section.  

    *update* Heroku doesn't think Django is installed and that is causing a deploy error.  I tried uninstalling from pip and reinstalling from pipenv as suggested in the readme, but so far that has not solved the issue.  Failing to get a successful deploy is probably my biggest challenge.  I redeployed under another app, lambda-reviews1 and that seems to have worked.  

  - How far did you get?
    I think I have my project deployed.  I haven’t yet been able to interact with it, since we were given no instructions on that, but Heroku gave me confirmation that my deploy was successful. 

    On second look though, while my upload was a success, the app site didn't work.  I then refactored and created a new app that 'may' work.  (I'm not sure what the final result should look like)

- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful? 
  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past. 
    I liked the Django docs, especially those listing the different fields available for models.  It was nice having all of the options listed out in one place without having to dig around the site to find out about different types of fields (like date vs text).  

    While I didn’t use any new fields in my models, these docs empowered me to try something a little different in my project.  I used Django validators (min and max) to customized my rating field.  


