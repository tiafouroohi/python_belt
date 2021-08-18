# python_belt
Python Belt created using Python/Django 

The code in this repository is for a job board application where users can register and log in to accounts, create job postings, edit, or delete them. 

A user may register for an account- if it does not satisfy the requirements, validations are set in place such that a user cannot create an account (i.e. password must be at least 8 characters long, a name must be at least 3 characters long).

Once a user registers or logs into an account, they are shown a dashboard of their account, as well as all jobs posted, and jobs the user posted.

A user is able to either create an account, or log into an account. Validators will appear if the login/registration does not satisfy requirements (i.e a name must be at least 3 characters long, an email must be a valid email, etc).

The user may create a job. If they desire, they may also edit a job. If a user views job details, it will show specific details such as the title, description, location, who posted the job, and when it was posted. If a user deletes a job, it will delete from all users. A job ID is attached to each job to show that it is deleted out of the database.

