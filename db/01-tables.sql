drop table if exists EssayEvaluation;
drop table if exists Class_;
drop table if exists ExtraMaterial;
drop table if exists Order_;
drop table if exists Plan;
drop table if exists CourseModule;
drop table if exists ModuleContent;
drop table if exists Consumption;
drop table if exists Comment_;
drop table if exists Evaluation;
drop table if exists QuestionAnswer;
drop table if exists Option_;
drop table if exists Question;
drop table if exists Exercise;
drop table if exists Content_;
drop table if exists Module_;
drop table if exists Essay;
drop table if exists Course;
drop table if exists Product;
drop table if exists CreditCard;
drop table if exists Student;

CREATE TABLE Student 
( 
 password_ VARCHAR,  
 name_ VARCHAR,  
 email VARCHAR,  
 studentId INTEGER PRIMARY KEY
); 

CREATE TABLE CreditCard 
( 
 cardNumber VARCHAR,  
 validThrough DATE,  
 ownerName VARCHAR,  
 securityNumber VARCHAR,  
 creditcardId INTEGER PRIMARY KEY
); 

CREATE TABLE Product 
( 
 name_ VARCHAR,  
 price FLOAT,  
 description VARCHAR,  
 productId INTEGER PRIMARY KEY
); 

CREATE TABLE Essay 
( 
 title VARCHAR,  
 theme VARCHAR,  
 text_ VARCHAR,  
 submitedAt DATE,  
 studentId INTEGER,  
 essayId INTEGER PRIMARY KEY,
 FOREIGN KEY(studentId) REFERENCES Student (studentId)
); 

CREATE TABLE EssayEvaluation 
( 
 comment_ VARCHAR,  
 rate FLOAT,  
 teacherName VARCHAR,  
 essayId INTEGER,  
 essayevaluationId INTEGER PRIMARY KEY,
 FOREIGN KEY(essayId) REFERENCES Essay (essayId)
); 

CREATE TABLE Course 
( 
 description VARCHAR,  
 title VARCHAR,  
 courseId INTEGER PRIMARY KEY
); 

CREATE TABLE Module_ 
( 
 title VARCHAR,
 description VARCHAR,  
 moduleId INTEGER PRIMARY KEY
); 

CREATE TABLE Content_ 
( 
 title VARCHAR,  
 description VARCHAR,  
 free_ BOOLEAN,  
 contentId INTEGER PRIMARY KEY
); 

CREATE TABLE Exercise 
( 
 contentId INTEGER,  
 exerciseId INTEGER PRIMARY KEY,
 FOREIGN KEY(contentId) REFERENCES Content_ (contentId)
); 

CREATE TABLE Class_ 
( 
 duration INT,  
 videoUrl VARCHAR,  
 contentId INTEGER,  
 classId INTEGER PRIMARY KEY,
 FOREIGN KEY(contentId) REFERENCES Content_ (contentId)
); 

CREATE TABLE ExtraMaterial 
( 
 pdfUrl VARCHAR,  
 contentId INT,  
 extramaterialId INTEGER PRIMARY KEY,
 FOREIGN KEY(contentId) REFERENCES Content_ (contentId)
); 

CREATE TABLE Question 
( 
 difficulty INT,  
 name_ VARCHAR,  
 position_ INT,  
 exerciseId INT,  
 questionId INTEGER PRIMARY KEY,
 FOREIGN KEY(exerciseId) REFERENCES Exercise (exerciseId)
); 

CREATE TABLE Option_ 
( 
 name_ VARCHAR,  
 correct BOOLEAN,  
 position_ INT,  
 questionId INTEGER,  
 optionId INTEGER PRIMARY KEY,
 FOREIGN KEY(questionId) REFERENCES Question (questionId)
);

CREATE TABLE Order_ 
( 
 orderedAt timestamp,  
 installments INTEGER,
 orderId INTEGER PRIMARY KEY,
 studentId INTEGER,  
 creditcardId INTEGER,
 productId INTEGER,
 FOREIGN KEY(productId) REFERENCES Product (productId),
 FOREIGN KEY(studentId) REFERENCES Student (studentId),
 FOREIGN KEY(creditcardId) REFERENCES CreditCard (creditcardId)
);

CREATE TABLE Plan 
( 
 courseId INTEGER,  
 productId INTEGER,
 FOREIGN KEY(courseId) REFERENCES Course (courseId),
 FOREIGN KEY(productId) REFERENCES Product (productId)
); 

CREATE TABLE CourseModule 
( 
 courseId INTEGER,  
 moduleId INTEGER,
 FOREIGN KEY(courseId) REFERENCES Course (courseId),
 FOREIGN KEY(moduleId) REFERENCES Module_ (moduleId)
); 

CREATE TABLE ModuleContent 
( 
 moduleId INTEGER,  
 contentId INTEGER,
 FOREIGN KEY(contentId) REFERENCES Content_ (contentId),
 FOREIGN KEY(moduleId) REFERENCES Module_ (moduleId)
); 

CREATE TABLE Consumption 
( 
 consumedAt timestamp,  
 studentId INTEGER,  
 contentId INTEGER,
 FOREIGN KEY(contentId) REFERENCES Content_ (contentId),
 FOREIGN KEY(studentId) REFERENCES Student (studentId)
); 

CREATE TABLE Comment_ 
( 
 commentedAt DATE,  
 text_ VARCHAR,  
 studentId INTEGER,  
 contentId INTEGER,
 FOREIGN KEY(contentId) REFERENCES Content_ (contentId),
 FOREIGN KEY(studentId) REFERENCES Student (studentId)
); 

CREATE TABLE Evaluation 
( 
 rate INTEGER,  
 evaluatedAt DATE,  
 studentId INTEGER,  
 contentId INTEGER,
 FOREIGN KEY(studentId) REFERENCES Student (studentId),
 FOREIGN KEY(contentId) REFERENCES Content_ (contentId)
); 

CREATE TABLE QuestionAnswer 
( 
 studentId INTEGER,  
 optionId INTEGER,
 FOREIGN KEY(studentId) REFERENCES Student (studentId),
 FOREIGN KEY(optionId) REFERENCES Option_ (optionId)
); 

--insert into Tabela values('v1', '123', 'texto');
/*TABELAS
Class_ 
Comment_ 
Consumption 
Content_ 
Course 
CourseModule 
CreditCard 
Essay 
EssayEvaluation 
Evaluation 
Exercise 
ExtraMaterial 
ModuleContent 
Module_ 
Option_ 
Order_ 
Plan 
Product 
Question 
QuestionAnswer
Student 
*/
