<html>
  <head>
    <title>RT Tagging</title>
  </head>
  <body>
    <form action="send.py" method="post">
        <h1>Support</h1>
        <hr>
        <h2>Problem type</h2>
        <select name="problem_type" id="id_problem_type">
          <option value="" selected>(select problem type)</option>
          <option value="accessing">Logging in or accessing the system</option>
          <option value="jobs">Running jobs</option>
          <option value="installed_software">Using installed software</option>
          <option value="software_request">Request for software installation</option>
          <option value="storage">Using storage</option>
          <option value="allocation">Resource allocation (core-hours, disk space, project duration etc)</option>
          <option value="supr">Using the SUPR portal</option>
          <option value="other">Other issues</option>
        </select>
    
       <h2>Centre and Resource</h2>
       If your problem is not related to a
       centre or a resource, you do not have to select something here.</p>
       <p>If your problem is related to a specific resource at a
         centre, select that. If your problem is related to multiple
         resources at a centre (or no resource listed here at all),
         select the centre and mention the resources in the problem
         description below.
      </p>  
      <select name="centre_resource" id="id_centre_resource">
        <option value="" selected>(select centre or resource)</option>
        <option value="c6">C3SE</option>
        <option value="r75">_ Alvis</option>
        <option value="r68">_ Cephyr NOBACKUP</option>
        <option value="r82">_ Mimer</option>
        <option value="r63">_ Vera</option>
        <option value="r43">_ Cstor no-backup</option>
        <option value="r35">_ Hebbe</option>
        <option value="c1">HPC2N</option>
        <option value="r49">_ Kebnekaise</option>
        <option value="c11">LUMI Sweden</option>
        <option value="c5">LUNARC</option>
        <option value="r44">_ Aurora</option>
        <option value="r70">_ Centrestorage nobackup</option>
        <option value="r24">_ Erik</option>
        <option value="c3">NSC</option>
        <option value="r79">_ Berzelius Compute</option>
        <option value="r80">_ Berzelius Storage</option>
        <option value="r45">_ Centre Storage</option>
        <option value="r62">_ Sigma</option>
        <option value="r61">_ Tetralith</option>
        <option value="c7">PDC</option>
        <option value="r30">_ Beskow</option>
        <option value="r71">_ Klemming</option>
        <option value="r37">_ Tegner</option>
        <option value="c10">SSC</option>
        <option value="r73">_ Cirrus</option>
        <option value="r55-west-1">_ Cloud region WEST-1</option>
        <option value="r55-north-1">_ Cloud region NORTH-1</option>
        <option value="r55-east-1">_ Cloud region EAST-1</option>
        <option value="r74">_ Dis</option>
        <option value="c9">Swestore</option>
        <option value="r31">_ dCache</option>
        <option value="r32">_ iRODS</option>
        <option value="c4">UPPMAX</option>
        <option value="r48">_ Bianca</option>
        <option value="r46">_ Irma</option>
        <option value="r83">_ Miarka</option>
        <option value="r51">_ Rackham</option>
        <option value="r60">_ Snowy</option>
        <option value="r84">_ Vulpes</option>
        <option value="r40">_ Fysast1</option>
        <option value="r28">_ Milou</option>
        <option value="r39">_ Smog</option>
        <option value="r20">_ Tintin</option>
        <option value="r34">_ topolino</option>
      </select>

    <h2>Project</h2>
      <p>If your problem is related to a specific project, select
        that.
      </p>  
    <select name="project" id="id_project">
      <option value="" selected>(select project if appropriate)</option>
      <option value="p18897">SNIC 2021/5-261: &quot;SNIC systems access for application experts&quot;</option>
      <option value="p11111">Test project</option>
    </select>

    <h2>Summary</h2>
      <p>Provide a concise one-line summary of your problem. It will be used
        as the subject line in emails about this problem. A good summary makes
        it easier for the issue to reach the correct persons.
      </p>
      <p>Do not use only generic phrases like "Help", "Problem", "Question", etc.</p>
    <input type="text" name="summary" maxlength="254" id="id_summary" />    

    <h2>Description</h2>
    <textarea class="form-control form-control-sm" name="description" cols="40" rows="10" id="id_description">
    </textarea>

    <input value="Send" type="submit" />
    </form>
  </body>
</html>
