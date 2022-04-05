<html>
  <head>
    <title>RT Tagging</title>
  </head>
  <body>
    <form action="send.py" method="post">
        <h1>Support</h1>
        <hr>
        Username: <input name="id_username" id="id_username" type="text" /><br><br>
        Mail: <input name="id_mail" id="id_mail" type="text" /><br><br>
        <h2>Problem type</h2>
        {{problem_type}}
    
       <h2>Centre and Resource</h2>
       If your problem is not related to a
       centre or a resource, you do not have to select something here.</p>
       <p>If your problem is related to a specific resource at a
         centre, select that. If your problem is related to multiple
         resources at a centre (or no resource listed here at all),
         select the centre and mention the resources in the problem
         description below.
      </p>  
      {{centre_resource}}

      <h2>Category</h2>
      {{category_type}}

      <h2>Project</h2>
        <p>If your problem is related to a specific project, select
          that.
        </p> 
      {{project}}

      <h2>Summary</h2>
        <p>Provide a concise one-line summary of your problem. It will be used
          as the subject line in emails about this problem. A good summary makes
          it easier for the issue to reach the correct persons.
        </p>
        <p>Do not use only generic phrases like "Help", "Problem", "Question", etc.</p>
      <input type="text" name="id_summary" maxlength="254" id="id_summary" />    

      <h2>Description</h2>
      <textarea name="id_description" cols="40" rows="10" id="id_description">
      </textarea><br><br>

    <input value="Send" type="submit" />
    </form>
  </body>
</html>
