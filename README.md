<p align="center">
  <img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201104T233040Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7bd49229be5713db15ccf8119177d84cd87a4e24372de1db4a01f1d512409e2c" alt="" style="">
 <h1 align="center"> The Holberton B&B </h1>
 <br>
 <p align="center">
 </p>
</p>

This project is divided into several parts. In this module a command interpreter is made to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

But the goal general is to deploy on your server a simple copy of the AirBnB website, but you do not implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

## Description
    
This module called the console is the first segment of the AirBnB project at Holberton School and its tasks are the following:

<ul>
    <li>Create your data model</li>
    <li>Manage (create, update, destroy, etc) objects via a console / command interpreter</li>
    <li>Store and persist objects to a file (JSON file)</li>
</ul>

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

## Installation

<ul>
    <li>Clone this repository: <pre><code>git clone https://github.com/santiagoPinzonD/AirBnB_clone.git</code></pre></li>
    <li>Access the created folder: <pre><code>cd AirBnB_clone</code></pre></li>
</ul>

This project can be worked in interactive or non-interactive mode as follows:

<ul>
    <li>Running in interactive mode: <pre><code>./console.py</code></pre></li>
    <li>Running in no interactive mode: <pre><code>echo "&lt;command&gt;" | ./console.py</code></pre></li>
</ul>

## Execution

In interactive mode:
<pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</code></pre>

In no interactive mode:
<pre><code>$ echo "help" | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
</code></pre>

## Classes

> PIA: PUBLIC INSTANCE ATTRIBUTES
> PIM: PUBLIC INSTANCE METHODS
> PCA: PUBLIC CLASS ATTRIBUTES
> PRCA: PRIVATE CLASS ATTRIBUTES

|Info|BaseModel|Amenity|City|State|Place|Review|User|FileStorage|
|---|---|---|---|---|---|---|---|---|
|PIA|id<br>created_at<br>updated_at|Inherits from<br>BaseModel|Inherits from<br>BaseModel|Inherits from<br>BaseModel|Inherits from<br>BaseModel|Inherits from<br>BaseModel|Inherits from<br>BaseModel| |
|PIM|save<br>to_dict|| | | | | |all<br>new<br>save<br>reload|
|PCA||name|state_id<br>name|name|city_id user_id name description number_rooms number_bathrooms max_guest price_by_night latitude longitude amenity_ids|place_id user_id text|email<br>password<br>first_name<br>last_name| |
|PRCA| | | | | | | |file_path objects|

## :file_folder: Files

| File Name / Folder Name | Content |
|---|---|
|[base_model.py](./models/base_model.py)|BaseModel Class|
|[amenity.py](./models/amenity.py)|Amenity Class|
|[city.py](./models/city.py)|City Class|
|[place.py](./models/place.py)|Place Class|
|[state.py](./models/state.py)|State Class|
|[review.py](./models/review.py)|Review Class|
|[user.py](./models/user.py)|User Class|
|[file_storage.py](./models/engine/file_storage.py)|FileStorage Class|
|[tests/test_models/](./tests/test_models/)|Unittests for BaseModel, User, Amenity, City, Place, Review, and State classes|
|[tests/test_models/test_engine/](./tests/test_models/test_engine/)|Unittest for FileStorage Class|

## Commands

| Command | Description |
|---|---|
|quit|Exit command interpreter|
|EOF|Exit command interpreter|
|create|Creates an instance|
|show|Displays all attributes of an instance|
|all|Displays all attributes of all instances|
|destroy|Deletes all attributes of an instance|
|update|Updates one attribute of an instance|

## Authors

<ul>
    <li><a href="https://twitter.com/santiagopinzonD" target="_blank">Santiago Pinzón</a></li>
    <li><a href="https://twitter.com/oscardeleon95" target="_blank">Oscar De León</a></li>
</ul>