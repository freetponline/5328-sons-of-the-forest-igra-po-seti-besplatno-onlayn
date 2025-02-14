var smilesTextarea = null;
var smilesIsLoaded = false;
function SmilesDoCall(obj) {
	window.smilesTextarea = document.getElementById(selField);
	$("body").append('<div style="display:none" id="smiles_dialog" title="Смайлики"></div>');
	$("#smiles_dialog").dialog({
		autoOpen: true,
		dialogClass: 'smiles_dialog',
		width: 400,
	});
	if(!smilesIsLoaded) {
		$.get(dle_root+"engine/ajax/smiles.php", null, function(data){
			window.smilesIsLoaded = true;
			$("#smiles_dialog").html(data);
		});
	}
}