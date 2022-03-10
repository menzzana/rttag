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
        <select name="id_problem_type" id="id_problem_type">
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
      <select name="id_centre_resource" id="id_centre_resource">
        <option value="" selected>(select centre or resource)</option>
        <option value="C3SE">C3SE</option>
        <option value="Alvis">_ Alvis</option>
        <option value="rCephyr NOBACKUP">_ Cephyr NOBACKUP</option>
        <option value="Mimer">_ Mimer</option>
        <option value="Vera">_ Vera</option>
        <option value="Cstor no-backup">_ Cstor no-backup</option>
        <option value="Hebbe">_ Hebbe</option>
        <option value="HPC2N">HPC2N</option>
        <option value="Kebnekaise">_ Kebnekaise</option>
        <option value="LUMI Sweden">LUMI Sweden</option>
        <option value="LUNARC">LUNARC</option>
        <option value="Aurora">_ Aurora</option>
        <option value="Centrestorage nobackup">_ Centrestorage nobackup</option>
        <option value="Erik">_ Erik</option>
        <option value="NSC">NSC</option>
        <option value="Berzelius Compute">_ Berzelius Compute</option>
        <option value="Berzelius Storage">_ Berzelius Storage</option>
        <option value="Centre Storage">_ Centre Storage</option>
        <option value="Sigma">_ Sigma</option>
        <option value="Tetralith">_ Tetralith</option>
        <option value="PDC">PDC</option>
        <option value="Beskow">_ Beskow</option>
        <option value="Klemming">_ Klemming</option>
        <option value="Tegner">_ Tegner</option>
        <option value="SSC">SSC</option>
        <option value="Cirrus">_ Cirrus</option>
        <option value="Cloud region WEST-1">_ Cloud region WEST-1</option>
        <option value="Cloud region NORTH-1">_ Cloud region NORTH-1</option>
        <option value="Cloud region EAST-1">_ Cloud region EAST-1</option>
        <option value="Dis">_ Dis</option>
        <option value="Swestore">Swestore</option>
        <option value="dCache">_ dCache</option>
        <option value="iRODS">_ iRODS</option>
        <option value="UPPMAX">UPPMAX</option>
        <option value="Bianca">_ Bianca</option>
        <option value="Irma">_ Irma</option>
        <option value="Miarka">_ Miarka</option>
        <option value="Rackham">_ Rackham</option>
        <option value="Snowy">_ Snowy</option>
        <option value="Vulpes">_ Vulpes</option>
        <option value="Fysast1">_ Fysast1</option>
        <option value="Milou">_ Milou</option>
        <option value="Smog">_ Smog</option>
        <option value="Tintin">_ Tintin</option>
        <option value="topolino">_ topolino</option>
      </select>

    <h2>Category</h2>
    <select id="id_category" name="id_category">
      <option value="Agricultural science">Agricultural science</option>
      <option value="Agricultural science forestry and fishing">Agricultural science forestry and fishing</option>
      <option value="Animal science">Animal science</option>
      <option value="Art">Art</option>
      <option value="Biological sciences">Biological sciences</option>
      <option value="Chemistry">Chemistry</option>
      <option value="Cinical medicine">Cinical medicine</option>
      <option value="Communikation science">Communikation science</option>
      <option value="Data- and information science)">Data- and information science)</option>
      <option value="Economics">Economics</option>
      <option value="Educational science">Educational science</option>
      <option value="Electrotechnological science and electronics">Electrotechnological science and electronics</option>
      <option value="Environmental biotechnology">Environmental biotechnology</option>
      <option value="Geosciences">Geosciences</option>
      <option value="Health science">Health science</option>
      <option value="Humanities">Humanities</option>
      <option value="Industrial biotechnology">Industrial biotechnology</option>
      <option value="Law">Law</option>
      <option value="Material science">Material science</option>
      <option value="Mathematic">Mathematic</option>
      <option value="Mechanical science">Mechanical science</option>
      <option value="Medical biotechnology">Medical biotechnology</option>
      <option value="Medical science">Medical science</option>
      <option value="Medical technology">Medical technology</option>
      <option value="Nanotechnology">Nanotechnology</option>
      <option value="Natural resources technology">Natural resources technology</option>
      <option value="Natural sciences">Natural sciences</option>
      <option value="Other technology">Other technology</option>
      <option value="Philosophical ethics and religion">Philosophical ethics and religion</option>
      <option value="Physics">Physics</option>
      <option value="Political science">Political science</option>
      <option value="Programming language">Programming language</option>
      <option value="Psychoology">Psychoology</option>
      <option value="Social and economic geography">Social and economic geography</option>
      <option value="Social science">Social science</option>
      <option value="Sociology">Sociology</option>
      <option value="Software">Software</option>
      <option value="Technological chemistry">Technological chemistry</option>
      <option value="Technological science">Technological science</option>
      <option value="Veterinary science">Veterinary science</option>
    </select>
    <h2>Project</h2>
      <p>If your problem is related to a specific project, select
        that.
      </p>  
    <select name="id_project" id="id_project">
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
    <input type="text" name="id_summary" maxlength="254" id="id_summary" />    

    <h2>Description</h2>
    <textarea class="form-control form-control-sm" name="id_description" cols="40" rows="10" id="id_description">
    </textarea><br><br>

    <input value="Send" type="submit" />
    </form>
  </body>
</html>
