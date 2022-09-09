# Employee Attrition Predictor

‘People Charm’, a growing company is facing a high attrition rate among their employees which in turn affects their business due to lack of expertise and experience. Their HR department is assigned the task to reduce the attrition rate by retaining employees who are about to churn out. They need to recommend special plans or strategies which will help them to retain their employees which in turn will help them to grow bigger as a company.

![image](https://user-images.githubusercontent.com/88525549/189327491-e8a02449-b822-429f-ade0-a4f4bf575419.png)

The file ‘People Charm Case.csv’ has several attributes. </b>

![image](https://user-images.githubusercontent.com/88525549/189324405-099c7e6f-c250-4529-ab6f-777f1eb30b62.png)

Understanding the problem
1. An attrition rate is a metric used to measure employees or customers lost over a period of time who are not replaced.

2. “People Charm, a growing company is facing a high attrition rate among their employees ”- means the company is losing lots of their employees over the years and they want to reduce this rate by finding strategies that can help them retain their employees which in turn will help them to grow bigger as a company.

3. In order to plan strategies, they have provided a dataset containing various attributes.

4. We need to find the best fit model which can predict if a certain employee will work in the company for a longer period, or if he/she is planning to leave the   company.

5. Using these predictions, the company can make their plans to avoid attrition.

6. This is a Binary Classification Problem

The aim of this project is to predict the chances of an employee leaving the company using people charm dataset, where there are certain parameters given to design an appropriate prediction model based on the employee's performance and the privilages he/she gets from the organization. For simplicity sake, the prediction model which I have used here is Random Forest Classifier which has the prediction score of 98.6.

![score](https://user-images.githubusercontent.com/88525549/189329087-a12216a6-2b62-4701-89e7-16bffe6f9dd4.png)

The project was  developed and deployed as an web-app using flask. Flask is a micro framework for web-applications writtenin python.
It consists of features such as login and signup, forgot password option, authentications and the on the spot result declaration. 

1. Login Page where the user logins themselves with username and password they sign-uped. If the user is not registered and tries to login-error, the page will display an error message saying: "the user doesn't exists ".

![Login](https://user-images.githubusercontent.com/88525549/189329636-45fa4a05-bdac-4bfc-b404-c8c57b9a4ebc.png)

There is a signup link as well provided:

![Singup](https://user-images.githubusercontent.com/88525549/189330438-0223e43e-0197-4849-a335-9bde9355608a.png)

The login page also consists of forgot password. By clicking on the forgot password button, the user gets redirected to another page.

2. Here the user must enter the username and email id. The password will then be sent to them on their mail id.

![Forgot Password](https://user-images.githubusercontent.com/88525549/189330693-0acb0e5e-fc5e-412b-82ab-0f3c0055be7e.png)

3. The last page is the home page where the prediction takes place. By entering certain values in the given fields, the results of an employee leaving the company or not will be displayed at the bottom. 

![Home 1](https://user-images.githubusercontent.com/88525549/189330955-0f1a1f10-904e-48e0-9a3b-0ddd83fcef4b.png)

![Home 2](https://user-images.githubusercontent.com/88525549/189330977-810fde76-6a37-4d85-b581-83db140ba791.png)



