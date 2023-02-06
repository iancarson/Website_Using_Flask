<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Syed Zaid Ahmed Kashif Syed Zaid Ahmed Kashif (sl248)</td></tr>
<tr><td> <em>Generated: </em> 10/31/2022 4:54:15 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/sl248" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113641300/197415653-5c8f4148-5de2-4bd7-bc72-d40866d488e5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the updated method for calculated_cost()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113641300/197418045-19d32d1f-f376-4858-96e9-afe486b6c8bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the calculated values in dollars<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>with the initial cost put down to zero, for loop was implemented to<br>add the cost of the container, scoops, and toppings, function returns the calculated<br>cost of the ice cream in dollars.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113641300/197603826-214cf6a1-f705-46e6-abc9-538359f03aac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the exception being used when too many scoops selected<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p>exception for out-of-stock is raised when something is out of stock<div>exception for needs<br>cleaning is raised when the icecream machine needs cleaning&nbsp;<br></div><div>exception for&nbsp;<span style="font-size: 13px; background:<br>var(--q-dark);">InvalidChoiceException is raised when an invalid choice is picked</span><br></div><div><span style="font-size: 13px; background: var(--q-dark);">&lt;span<br>style=&quot;font-size: 14px;&quot;&gt;exception for&nbsp;</span><span style="background: var(--q-dark);">ExceededRemainingChoicesException raised when there are too many scoops of<br>icecream</span><br></span></div><div><span style="font-size: 13px; background: var(--q-dark);"><span style="background: var(--q-dark);"><span style="font-size: 14px;">exception for&nbsp;</span><span style="background: var(--q-dark);">InvalidPaymentException raised<br>when an invalid payment amount is given&nbsp;</span><br></span></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113641300/199100286-880f528a-938b-465e-846f-698f9c7c7d04.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test cases as per the checklist<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113641300/199100407-a03212bd-a3c2-45df-89ad-674459184b9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test cases as per the checklist<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113641300/199100497-0ff7c00b-64b2-42da-8d26-0d179e617c9d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test cases as per the checklist<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113641300/199100635-e7058e5d-a5d1-43bf-885c-6e03e2cb10ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test cases as per the checklist<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113641300/199100716-67e5e4f7-efd2-47b6-b851-bce8d8937d86.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test cases as per the checklist<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113641300/199100799-11678469-bf76-46df-af92-f607f3b799f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for test cases as per the checklist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>when the user inputs the valid selection from the options each item is<br>then added and further adds up to the total by repeating this process<br>until the selection is complete the final calculation is depicted in dollars for<br>the user to pay. &nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/zaid-kashif/IS-601/pull/5">https://github.com/zaid-kashif/IS-601/pull/5</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>concepts like loops, functions, and other concepts were implemented while executing the program,<br>and implementing them was fun but faced a little difficulty in exceptions.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113641300/197417444-d959ff5a-b39b-4471-8f87-283fe3f91ae1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of successful output for ice cream combination of waffle cone with<br>vanilla and strawberry scoop and peanuts as topping<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113641300/197417556-73dcd1f5-04c2-46bf-afe3-810e521f5e06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of successful output for ice cream combination of sugar cone with<br>chocolate and strawberry scoop and m&amp;ms with sprinkles as topping<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113641300/197417651-79c8cc76-b6ef-4325-8924-8621121e3a31.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of successful output for ice cream combination of cup with vanilla<br>and strawberry scoop with peanuts and gummy bears as topping<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/sl248" target="_blank">Grading</a></td></tr></table>