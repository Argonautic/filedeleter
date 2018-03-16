# filedeleter

<p>Delete files from a directory and subdirectories, using a csv file as a blacklist (files to delete) or whitelist (files to keep).</p>

<h2>How To Use</h2>
<p>
  Currently, filedeleter is designed as a command-line app, and the best way to use it is to clone or download this
  repository and run the app directly using <b>python3 filedeleter.py</b>. For ease of use, you may want to add a PATH to
  your downloaded/cloned directory. All this to be automated in the future, or added to pip (if such a library doesn't    already
  exist).
  <br><br>
  The only functional file is filedeleter.py, all other files and directories are just for testing and example. Python 2 version can be made if anyone wants it.
  <br><br>
  Command line arguments are as follows:
</p>

<h3>Required</h3>
<table>
  <tr>
    <th>
      Argument
    </th>
    <th>
      Description
    </th>
  </tr>
  <tr>
    <td>
      csvPath
    </td>
    <td>
      The path of the csv file to read from
    </td>
  </tr>
</table>

<h3>Optional</h3>
<table>
  <tr>
    <th>
      Argument
    </th>
    <th>
      Description
    </th>
  </tr>    
  <tr>
    <td>
      -dPath
    </td>
    <td>
      The directory in which to start deletion (defaults to cwd)
    </td>
  </tr>
  <tr>
    <td>
      -cName
    </td>
    <td>
      The name of the csv column that identifies filenames (defaults to "Filenames")
    </td>
  </tr>
  <tr>
    <td>
      -w
    </td>
    <td>
      Whitelist - keep only files listed in csv and delete everything else
    </td>
  </tr>
  <tr>
    <td>
      -s
    </td>
    <td>
      Shallow delete - only delete in directory at -dPath, disregard subdirectories
    </td>
  </tr>
</table>
