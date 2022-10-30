# AirBnb Clone - The Console

## Authors
* [Adonyas Getachew](Adonyas2000@gmail.com)
* [Mintesnot Tsegaye]()

## Table of Contents

- [Description of the Project](#description-of-the-project)
- [Description of the Console](#description-of-the-console)
- [How to Start It](#how-to-start-it)
- [How to Use It](#how-to-use-it)
- [Examples](#examples)

## Description of the Project

The 'AirBnb Clone - The Console' project served as an introduction to creating a full web application based on AirBnb. In this step, we focused on building the foundation for future aspects of our project (HTML/CSS templating, database storage, API, and front-end integration). 

Each task in this project was used to help achieve the following:

* Create a parent class (called BaseModel) to take care of the initialization, serialization, and deserialization of future instances.

* Create a simple flow of serialization/deserialization
	* Instance <-> Dictionary <-> JSON String <-> File

* Create classes for AirBnb application that inherit from BaseModel
	* User
	* State
	* City
	* Place
	* Review
	* Amenity

* Create a file storage for storage engine use.
	* FileStorage Class

* Create unittests to validate all classes and the storage engine.

## Description of the Console

Working hand in hand with the components that we built for our project (BaseModel, FileStorage, etc.), the console will be used for access of the functionalities offered by our components. 

For example, we will be able to achieve the following with our console:

* Create a new object
* Retrieve an object from a file, database, etc.
* Perform operations on objects
* Update attributes of objects
* Destroy objects
* Display all objects or objects of a certain class

## How to Start It

Prior to using our console, please ensure that all files from the master branch have been downloaded on your local computer. Once this step is complete, the following command can be entered into terminal and the console program will begin:

**./console.py**

## How to Use It

The following commands are available in the console:

* **create**
	* This command creates a new instance of the specified class. The new instance of the specified class is saved to a JSON file and the id is printed to the standard output. 
		* If the class name is missing, the message '\*\* class name missing \*\*' will be printed.
		* If the class name does not exist, the message '\*\* class doesn't exist \*\*' will be printed.

* **show**
	* Given the class name and id of an instance, this command will print the string representation of the specified instance. 
		* If the class name is missing, the message '\*\* class name missing \*\*' will be printed.
		* If the class name does not exist, the message '\*\* class doesn't exist \*\*' will be printed.
		* If the id is missing, the message '\*\* instance id missing \*\*' will be printed.
		* If the instance of the class name does not exist for the given id, the message '\*\* no instance found \*\*' will be printed.

* **destroy**
	* Given the class name and id of an instance, this command will delete the specified instance.
		* If the class name is missing, the message '\*\* class name missing \*\*' will be printed.
		* If the class name does not exist, the message '\*\* class doesn't exist \*\*' will be printed.
		* If the id is missing, the message '\*\* instance id missing \*\*' will be printed.
		* If the instance of the class name does not exist for the given id, the message '\*\* no instance found \*\*' will be printed.

* **all**
	* Given the class name, this command will print the string representation of all instances under the specified class. If no class name is specified, all existing objects will be printed. 
		* The printed result will be in a list of strings.
		* If the class name does not exist, the message '\*\* class doesn't exist \*\*' will be printed. 

* **update**
	* Given the class name, id, attribute name, and attribute value, this command will update the attribute value of the specified instance. 	
		* If the class name is missing, the message '\*\* class name missing \*\*' will be printed.
		* If the class name does not exist, the message '\*\* class doesn't exist \*\*' will be printed.
		* If the id is missing, the message '\*\* instance id missing \*\*' will be printed.
		* If the instance of the class name does not exist for the given id, the message '\*\* no instance found \*\*' will be printed.
		* If the attribute name is missing, the message '\*\* attribute name missing \*\*' will be printed.
		* If the value for the attribute is missing, the message '\*\* value missing \*\*' will be printed.
		* All arguments after the attribute value will be ignored.
		* Only attributes with values of a string, integer, or float type can be updated. 
* **count**
	* Given the class name, this command will print out the number of objects under the specified class. 

These commands can be recognized by one or two standardized formats. The available formats are as follows:

* create
	* create \<class name\>
* show
	* show \<class name\> \<id\>
	* \<class name\>.show(\<id\>)
* destroy
	* destroy \<class name\> \<id\>
	* \<class name\>.destroy(\<id\>)
* all
	* all \<class name\>
	* \<class name\>.all()
* update
	* update \<class name\> \<id\> \<attribute name\> \<attribute value\>
	* \<class name\>.update(\<id\>, \<attribute name\>, \<attribute value\>)
* count
	* \<class name\>.count()

## Examples

Once the command ./console.py has been typed into the terminal, the user will be prompted with (hbnb). The user can proceed to enter the commands that have been specified in the previous section into the terminal. Some examples are as follows:

* create
	* create BaseModel

* show
	* show BaseModel 0aafa26e-cacb-4669-be7d-791d03f9764b
	* Place.show(0aafa26e-cacb-4669-be7d-791d03f9764e)
* destroy
	* destroy BaseModel 0aafa26e-cacb-4669-be7d-791d03f9764b
	* City.destroy(0aafa26e-cacb-4669-be7d-791d03f9764b)
* all
	* all BaseModel
	* all
	* Amenity.all()
* update
	* update BaseModel
	* update BaseModel 0aafa26e-cacb-4669-be7d-791d03f9764b
* count
	* User.count()
	* BaseModel.count()
