import jinja2
import pdfkit

def createpdf():
    # nom_user= Etudiants.objects.get(id_user=user_id).etudiant_nom
    # prenom_user= Etudiants.objects.get(id_user=user_id).etudiant_prenom
    # type_stage_user= stage.code_type_id
    # tuteur_user= f"{Tuteurs.objects.get(tuteur_numero=stage.tuteur_id).tuteur_nom} {Tuteurs.objects.get(tuteur_numero=stage.tuteur_id).tuteur_prenom}"
    # entreprise_user= stage.siret_id

    nom_user='frde'
    prenom_user='trfe'
    type_stage_user='trfe'
    tuteur_user='ytvfdd'
    entreprise_user='ytvfdd'

    context = {
        'nom_user': nom_user,
        'prenom_user': prenom_user,
        'type_stage_user': type_stage_user,
        'tuteur_user': tuteur_user,
        'entreprise_user': entreprise_user
    }

    template_loader = jinja2.FileSystemLoader(searchpath="templates/stageform/")
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template('pdfstage.html')
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
    pdfkit.from_string(output_text, 'generated2pdf.pdf', configuration=config)

createpdf()