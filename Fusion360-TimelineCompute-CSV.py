#Author- schneik
#Description- Export timeline feature compute times as csv

import adsk.core, adsk.fusion, adsk.cam, traceback, os

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        docName = app.activeDocument.name

        feats = app.executeTextCommand("fusion.DumpFeaturesByComputeTime /csv")
        print(feats)
        
        # Set styles of file dialog.
        folderDlg = ui.createFolderDialog()
        folderDlg.title = "Choose Folder to save CSV file"

        # Show file save dialog
        dlgResult = folderDlg.showDialog()
        if dlgResult == adsk.core.DialogResults.DialogOK:
            filepath = os.path.join(folderDlg.folder, docName + ".csv")
            # Write the results to the file
            with open(filepath, "w") as f:
                f.write(feats)
            ui.messageBox("CSV file saved at: " + filepath)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
