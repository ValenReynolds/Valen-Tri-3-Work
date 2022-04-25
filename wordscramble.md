--- 
layout: default
permalink: /wordscramble/
---

[Home](../index)

# Documentation  
## Create Task Design
[Create Plan Design and Ideas](https://docs.google.com/document/d/14YG7ZscxqKMrEArx1GuzEqcIB_f6ZqT086UE8ttQ3lM/edit?usp=sharing)

## Valen Video - (Beach Guessing Game) 
[https://youtu.be/k9uUI4-word scramble](https://youtu.be/k9uUI4-Haeo)


## Overview of Word Scrambler
Word Scrambler is a game that presents a list of scrambled words that the player must guess. The game tracks correct and incorrect guesses, with the game ending once all words have been determined correctly. Based on how well the player performed, they receive a star rating between zero to five stars. While the game is designed to be initialized with any number of words, the star rating is fixed at zero to five. 

<img width="566" alt="Screen Shot 2022-02-28 at 10 12 56 AM" src="https://user-images.githubusercontent.com/89166851/156035835-60b9756e-987f-45bf-99b4-02b87b7008d1.png">
##  Setup
An array is initialized with the unscrambled words to be used during the game. 
Global variables for keeping score are initialized (totalscore, etc.)

<img width="282" alt="Screen Shot 2022-02-28 at 10 14 57 AM" src="https://user-images.githubusercontent.com/89166851/156036073-2e2c4ce6-5778-4005-ac4c-4390b7e0280a.png">

<img width="432" alt="Screen Shot 2022-02-28 at 10 15 19 AM" src="https://user-images.githubusercontent.com/89166851/156036117-580db9be-464b-4ecb-b248-43b2468e71f6.png">

## Game Initialization
The website is initialized by calling foo() which scrambles all the words in the word list creating a new array of scrambled words. The scrambled word list is turned into a string, which gets displayed to the player.
### Restart Game
The game can be restarted and re-initialized by refreshing the web browser. 
##  Game Play
The player enters a guess into the text box and either hits the Enter key or clicks on the Submit button. This triggers the javascript that processes the guess.
### Process Guesses
We iterate over the unscrambled word list and compare it to the guess provided by the player. 

<img width="939" alt="Screen Shot 2022-02-28 at 10 17 42 AM" src="https://user-images.githubusercontent.com/89166851/156036437-c3d68358-7af4-4769-bb82-5f063500ac4a.png">

### Guessed Correctly
If there is a match, then totalscore is updated and the correctly guessed word is removed from the list of available words. The scrambled version of the word guessed correctly is also removed from the list. 

<img width="691" alt="Screen Shot 2022-02-28 at 10 19 17 AM" src="https://user-images.githubusercontent.com/89166851/156036647-4bc1e523-407e-4792-bed9-f5c1e5a240ef.png">

### Guessed Incorrectly
The number of incorrect guesses is updated and the player is asked to try again. 

<img width="719" alt="Screen Shot 2022-02-28 at 10 20 44 AM" src="https://user-images.githubusercontent.com/89166851/156036882-c89adaeb-98eb-42fd-b8b3-b0e27831e0f0.png">

### Game Over
When all the words have been guessed correctly the player is informed that the game is over

<img width="790" alt="Screen Shot 2022-02-28 at 10 21 16 AM" src="https://user-images.githubusercontent.com/89166851/156036946-0d159508-1ddf-4527-b4fd-81ddc0fb6fd7.png">

### Final Score Rating
Based on how well the player did, they receive a zero to five gold star rating. 
The algorithm awards each star by changing the graphic from a grey star to a gold star.
All the stars are displayed at the end at once after the gold stars have been assigned. 

<img width="677" alt="Screen Shot 2022-02-28 at 10 22 45 AM" src="https://user-images.githubusercontent.com/89166851/156037157-74dbaaff-ea10-45b9-8739-3201dbb77baf.png">


## Future Work 
There are additional improvements that can be made to the game. In the future, I would make it where one word pops up at a time.
### Quitting
Allow the player to quit if they cannot guess the words. The player would get a final star rating based on how well they did up to the point they quit. 
### Long Word Lists
The game is designed to support as many words as we add to the initial array. The display however does not format very long strings. If the game is going to handle a lot of words then the user interfaces for presenting those words should be improved from the current comma-separated list on a single line. 

## HTML / CSS
### Background
Create a fancy background with a beach theme for our game. Make it tall wide enough.

<pre>
<code>
        div.background {
            background: url(https://images.unsplash.com/photo-1528784289209-d1bf7e951bcb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGFjaWZpYyUyMGJlYWNofGVufDB8fDB8fA%3D%3D&w=1000&q=80) no-repeat;
            background-size: cover;
            border: 10px solid black opacity: 0.7;
            min-width: 400px;
            min-height: 600px;
        }
</code>
</pre>

### Guessbox
We want a guessbox div so we can use styling features aimed at anything in that box.

<pre>
<code>
div.guessbox p {
            margin: 10%;
            font-weight: bold;
            color: #000000;
        }

### Stars Container
A container for all the star ratings that lets us hide and show them all as a group.

<pre>
<code>
 .stars {
            align-items: top;
            display: flex;
            height: 100vh;
            justify-content: center;
        }
</code>
</pre>

### Star Shape
This fancy code creates a star shape using a polygon. This was open-source code we found online. 50 pixels looks like a good size for our star. These stars are gold.

<pre>
<code>
        .clip-star {
            background: gold;
            clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
            display: inline-block;
            height: 50px;
            width: 50px;
            align-items: center;
        }
</code>
</pre>

### Star Shape 
Exactly the same as the gold star only this star has a grey background. Maybe I could have just used one shape and changed the background color? I was able to get it working by swapping shapes.

<pre>
<code>
        .clip-star-dark {
            background: #333;
            clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
            display: inline-block;
            height: 50px;
            width: 50px;
            align-items: center;
        }
</code>
</pre>

## Body 

### Initialize

This important line defines the body and also calls the javascript to initialize the game before the html page loads.
* body onload="initialize();

### Guessbox
The guessing box includes a scramble word label which is used to display all the scrambled words. It has a button that calls get guess() when pressed. It has a text box guess text where the player enters in each word guess. The label score is where the score is updated as the game is played.

### Stars
Our stars are initially all grey. They are hidden by the javascript that initializes the game. Later we turn them gold based on the scoring logic.

***
***


# Yash - (Tic Tac Toe) [Video](https://youtu.be/CTiaXashFsg)
[Written Responses](https://docs.google.com/document/d/1UIRmeW4Dpcra5GtODsZPwa_F4fTg7O7HcxUMnaSb_u4/edit?usp=sharing) \
<img width="407" alt="Screen Shot 2022-02-28 at 8 46 57 AM" src="https://user-images.githubusercontent.com/89223735/156023345-e65fab9b-a53e-4fab-8a55-f71059a18c0f.png"> \
<img width="556" alt="Screen Shot 2022-02-28 at 8 47 11 AM" src="https://user-images.githubusercontent.com/89223735/156023379-5a570eb0-6c70-46c1-8117-d6d50b8aef07.png"> \
<img width="1152" alt="Screen Shot 2022-02-11 at 11 40 00 AM" src="https://user-images.githubusercontent.com/89223735/153658420-a484a503-7275-4b42-82b8-7286e3e73b3d.png">

I got 2/3 because I misread the answer. I thought it meant that it breaks up the pieces in small bits. But it meant exponentially decreasing.

# Avinh - Wordle Game ([video](https://youtu.be/hP12Rj3pUEY))

### Input:

- Takes a 5 letter word guess from the user.
- Returns it to the doc through jinja

![image](https://user-images.githubusercontent.com/43688346/156037182-e4533812-f014-4d39-a694-26bd085f101a.png)

![image](https://user-images.githubusercontent.com/43688346/156036502-75fcde7c-8d07-4321-95ce-c7839651eab4.png)

![image](https://user-images.githubusercontent.com/43688346/156036667-f4663d45-0127-4635-b276-519c55e979c3.png)

![image](https://user-images.githubusercontent.com/43688346/156036622-b1965eee-fa90-45ff-b6b1-e950a6890cf5.png)

![image](https://user-images.githubusercontent.com/43688346/156037306-cd11b0de-9c7e-4e73-83ee-4cbcc5b5dd71.png)

### List:

List of all of the possible final words there can be.

![image](https://user-images.githubusercontent.com/43688346/156036824-00aabb0a-56df-4bc0-9c1d-f6cf873142e0.png)

### Procedure:

- Render function renders all of the squares with the text
- Procedure Name: Render
- Return Type: none
- Parameters: GuessList

![image](https://user-images.githubusercontent.com/43688346/156036895-4d20f599-c7ac-4f91-9b2a-1a6d4361b206.png)

### Algorithm:

- Sequencing: Iterates through each element in GuessList before iterating through each character for each element
- Iteration: Iterates through each element, and iterates through each character

![image](https://user-images.githubusercontent.com/43688346/156036929-72baae3a-8e50-4ada-bac3-d0d0a0f2c7d3.png)

- Selection: Declares variable GuessList if undefined, and pulls the variable from local storage if it is defined

![image](https://user-images.githubusercontent.com/43688346/156037006-fffdbf6d-0a85-4ce3-91af-9ae6ad8be451.png)

### Calls:

![image](https://user-images.githubusercontent.com/43688346/156037072-7682a021-9a24-4da3-aa6a-9703bc04ce62.png)

### Output: 

Renders the word and highlights green if the character is in the right spot, and yellow if it is present but in the incorrect spot

![image](https://user-images.githubusercontent.com/43688346/156037234-148e95ef-a0df-4476-8d57-7610122a4348.png)

***
***

# Jay - (Memory Game) [Video Link](https://youtu.be/IBTZKOMER5w)
### 3A 
**Overall purpose:** The overall purpose of the program is to provide a fun, beach-themed game, in which users can participate. The game is a classic matching game, through which the agents can enjoy themselves to a witty game. 
**Functionality/Input:** The functionality of the program is to essentially flip two cards over permanently depending on whether they are a match or not. If the cards are not a match, then they will flip over. However, if the agent picks two matching cards, they will receive an alert that tells them that got a match. The overall object of the game is to have all matching cards.
**Input/Output:** Essentially the input is the moves in which the agent chooses the cards in the game. The output would be the feedback received from the backend that lets the agent know if it was a match or not. If it was a match then the agent would be alerted with a message. 

### 3B
Storing Data in a List:

![list](https://user-images.githubusercontent.com/89176673/155947975-520b7929-4add-4196-a2b9-58fe719b32f4.PNG)

Using the Data:

![usinglist](https://user-images.githubusercontent.com/89176673/155948178-6960c95b-98cf-4441-8433-6bbcaec0cf31.PNG)


The list being used in this example is front images. The list manages complexity so that I do not have to keep restating the same content. Instead, the list is called once so that it is not repetitive, and more efficient. The list just refers to the ids that I have given to my images (1-11). 

### 3C
Procedure:

![3ci](https://user-images.githubusercontent.com/89176673/155948573-136b2b00-4c24-462e-a3f6-b5997c91e79c.PNG)


Calling the procedure:


![3cii](https://user-images.githubusercontent.com/89176673/155948659-6fba6dcc-4d17-4916-86d6-dd537b103303.PNG)

The procedure essentially iterates over the image data. Additionally, it prints to the debugger console. Overall the functionality is made more efficient because repetition is not required. 

**Detailed Description:** The algorithm starts off with a for loop which takes the variable "front image" from the array front images and prints it in the console. Then, if validate, ensures that there are no errors in the code and functionality. Then the first and second remove event listeners make it so that the images are flipped when they are clicked on. 
### 3D
**Call 1:** 
![call 1](https://user-images.githubusercontent.com/89176673/155948991-1cd93926-8afb-453a-a4dd-dd8f3d9d8d16.PNG)
The conditions which are being tested in the first call are whether or not the cards are matching. The cards are either permanently flipped or they are unflipped. In more general terms, they are either flipped or turned down. 
**Call 2:** 
The same condition is being tested by the second call, as to whether the cards are matching or not. This essentially determines the functionality of the overall process.

![call 2](https://user-images.githubusercontent.com/89176673/155949061-6a76cc32-7fa2-4eef-8327-abbd04dd5ca9.PNG)

# Akhil - Site Search Feature - [Video Link](https://youtu.be/98KXo33uTuY)
### [Final Commited Code](https://github.com/YashShah138/Team-MicrosoftTechSupport/blob/ee14dfae0d25b1812d7c171747f12bcc4982f839/templates/layouts/base.html#L44-L112)
### 3A 
**Overall purpose:** Navigate our Beach Resource Website easier by searching for pages.
**Functionality/Input:** Input text and submit into a search bar which returns a rendered HTML page based on what was searched for. Inputted invalid request for a page that does not exist and an error message is displayed with a prompt that includes an example of what to search for.
**Input/Output:** Text is inputted, rendered HTML page or error message is outputted.

### 3B
Storing Data in a List:

<img width="584" alt="Screen Shot 2022-02-14 at 11 07 01 AM" src="https://user-images.githubusercontent.com/89219514/153929719-5b4d9f67-8d41-403a-8c74-a664aaa18083.png">

Using the Data:

<img width="1011" alt="Screen Shot 2022-02-14 at 11 08 21 AM" src="https://user-images.githubusercontent.com/89219514/153929873-dbe1e322-4932-439a-a93c-4df032a9a401.png">

The list being used in this example is beach pages. The other lists can be used by changing the function's used parameter value. The data in the list is organized as a dictionary, and each item in the list represents the name of one of the beach pages and its corresponding URL. The list is used to manage complexity by organizing all of the pages into a list that can be iterated through. This makes searching for the desired list easy by iterating through each item and checking whether it matches the user's input. Without using a list like this, searching all of the pages and their URLs would not be possible. 

### 3C
Procedure:

<img width="1006" alt="Screen Shot 2022-02-14 at 11 16 09 AM" src="https://user-images.githubusercontent.com/89219514/153930922-2a556827-2c0a-4f89-8ef5-7f26c0caaa15.png">

Calling the procedure:

<img width="837" alt="Screen Shot 2022-02-14 at 11 17 17 AM" src="https://user-images.githubusercontent.com/89219514/153931049-79f06f38-2d21-4406-ae52-1d51f728f3e2.png">

The general function of the procedure recognizes the user's input into a text box, searches the dictionary for a matching beach page, and returns the link of the page. 

**Detailed Description:** variable "x" contains the dictionary data as JSON information. Variable "input" gets the user's input from the HTML search bar with the id "beach search". The input is turned to lowercase to prevent case sensitivity. A for loop sets an index marker at position 0, and loops the following instructions _n_ number of times where _n_ is the length of the list "beach pages": The algorithm checks if the substring of the input from index 0 to the length of the input matches any item in the dictionary using the same substring method. This allows a valid return even if the user does not enter the entire name of the page. If true, the variable "link" gets assigned to the corresponding URL page and is returned. If none of the items in the list match the input, an error message is displayed and gives an example using a random number function to pick a random index in the valid list to display as an example.

### 3D
**Call 1:** Search bar takes the input of "Del Mar Beach", while function takes a parameter "beach pages", and submit button is pressed. Condition tested by the first call is if the input matches an item in the "beach pages" list. The result of this call would return a rendered page with the URL "/del-mar-beach/", and display the page. 

**Call 2:** Search bar takes the input of "Pacific Beach", while function takes a parameter "about pages", and submit button is pressed. Condition tested by the second call is if the input matches an item in the "about pages" list. The result of the call would not find a matching page in the list, and run the error code block, by returning the same page, and displaying an error message saying, "Page Does Not Exist. Please search for pages similar to: " and provides a random example of a page in "about pages".
