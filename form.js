// run event listener for when the google sheet is changed (worksheet added or deleted)
onChange()

// event listener onChange
function onChange() {
  getSpreadsheetData();
  makeOurForm();
}

function getSpreadsheetData() {
  // This function gives you an array of objects modeling a worksheet's tabular data, where the first items — column headers — become the property names.
  var sheets = SpreadsheetApp.getActiveSpreadsheet().getSheets();
  var arrayOfArrays = sheets[sheets.length - 1].getDataRange().getValues();
  var headers = arrayOfArrays.shift();
  return arrayOfArrays.map(function (row) {
    return row.reduce(function (memo, value, index) {
      if (value) {
        memo[headers[index]] = value;
      }
      return memo;
    }, {});
  });
}

function makeOurForm() {
  var form = FormApp.create('Boyz and jordan pickem v8')
  
  form.setDescription("I spent the week automating this process away. I didn't make this form, this script did. Lemme know if anything is messed up.");
  
  form.addTextItem().setTitle('Name').setRequired(true);
  form.addTextItem().setTitle('Email').setRequired(true);
  
  getSpreadsheetData().forEach(function (row) {
    var capitalizedName = row.home_team_name.charAt(0).toUpperCase() + row.home_team_name.slice(1);

    /*form.addSectionHeaderItem()
      .setTitle(capitalizedName);*/

    var item = form.addMultipleChoiceItem();
    if(row.wk_day == 'MON') {
      item.setTitle(row.away_team_name + ' (' + row.away_line + ') @ ' + row.home_team_name + ' [MNF]')
      .setChoices([
        item.createChoice(row.away_team_name),
        item.createChoice(row.home_team_name),
      ]).setRequired(true);
     } else if (row.wk_day == 'THU') {
       item.setTitle(row.away_team_name + ' (' + row.away_line + ') @ ' + row.home_team_name + ' [TNF]')
      .setChoices([
        item.createChoice(row.away_team_name),
        item.createChoice(row.home_team_name),
      ]).setRequired(true);
    } else {
      item.setTitle(row.away_team_name + ' (' + row.away_line + ') @ ' + row.home_team_name)
      .setChoices([
        item.createChoice(row.away_team_name),
        item.createChoice(row.home_team_name),
      ]).setRequired(true)
    }
  });
  
  form.addTextItem()
      .setTitle('ATS bonus').setRequired(true);
}