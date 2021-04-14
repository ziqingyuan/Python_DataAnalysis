#  Whether there is a difference in the alive percentage for marvel character with differents align (bad, neutral good) compare to the overall alive percentage?

### Where is the information from? 
- This dataset was originally collected based on Maval Wikia and created by FiveThrityEight, posted in Kaggle.  Some change has made for better and clearer analysis. 

### Why is it interesting to you?
- As we all know, Marvel cosmics mostly talks about superhero stories. It is interesting to look whether Stan Lee tend to give more chance for good character to be alive. 

### Explain how you used what you learned about systematic program design to solve the problem. 
##### We design some new data types (HtDD)
- Alive (bool) to represent whether a character is living or deceased 
- Align (Enumration) to represent the align that the charater belongs to (either bad, neutral or good)
- Marvel (Compound) to save the Alive and Align data of a character
- List[Marvel] to filter the data save in a csv file as a list of marvel data
##### We use the HtDF to write our functions
##### We use HtDaP to create a bunch of helper functions
- composition rule
- reference rule

### What design choices did you have to make? Why did you make the choices that you made?
- We have to choose the data each figure contains to make the clearest comparision
- We chose make 4 pie charts, 
 1. the overall alive percentage of all characters
 2. the alive percentage of all bad characters
 3. the alive percentage of all neutral characters
 4. the alive percentage of all good characters
 

- We made this choice because it will be clear to compare the alive percentage of all the characters with the alive percentage of characters form each aligns to know which align's characters tend to have more be alive
