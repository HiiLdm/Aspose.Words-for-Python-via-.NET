# Copyright (c) 2001-2023 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.

import aspose.words as aw

from api_example_base import ApiExampleBase, MY_DIR, ARTIFACTS_DIR

class ExSvgSaveOptions(ApiExampleBase):

    def test_save_like_image(self):

        #ExStart
        #ExFor:SvgSaveOptions.fit_to_view_port
        #ExFor:SvgSaveOptions.show_page_border
        #ExFor:SvgSaveOptions.text_output_mode
        #ExFor:SvgTextOutputMode
        #ExSummary:Shows how to mimic the properties of images when converting a .docx document to .svg.
        doc = aw.Document(MY_DIR + "Document.docx")

        # Configure the SvgSaveOptions object to save with no page borders or selectable text.
        options = aw.saving.SvgSaveOptions()
        options.fit_to_view_port = True
        options.show_page_border = False
        options.text_output_mode = aw.saving.SvgTextOutputMode.USE_PLACED_GLYPHS

        doc.save(ARTIFACTS_DIR + "SvgSaveOptions.save_like_image.svg", options)
        #ExEnd

    def test_save_office_math(self):
        #ExStart:SaveOfficeMath
        #GistId:a775441ecb396eea917a2717cb9e8f8f
        #ExFor:NodeRendererBase.save(string, SvgSaveOptions)
        #ExSummary:Shows how to pass save options when rendering office math.
        doc = aw.Document(file_name=MY_DIR + "Office math.docx")
        math = doc.get_child(aw.NodeType.OFFICE_MATH, 0, True).as_office_math()
        options = aw.saving.SvgSaveOptions()
        options.text_output_mode = aw.saving.SvgTextOutputMode.USE_PLACED_GLYPHS
        math.get_math_renderer().save(file_name=ARTIFACTS_DIR + "SvgSaveOptions.Output.svg", save_options=options)
        #ExEnd:SaveOfficeMath

    def test_max_image_resolution(self):
        #ExStart:MaxImageResolution
        #ExFor:ShapeBase.soft_edge
        #ExFor:SoftEdgeFormat.radius
        #ExFor:SoftEdgeFormat.remove
        #ExSummary:Shows how to set limit for image resolution.
        doc = aw.Document(file_name=MY_DIR + 'Rendering.docx')
        save_options = aw.saving.SvgSaveOptions()
        save_options.max_image_resolution = 72
        doc.save(file_name=ARTIFACTS_DIR + 'SvgSaveOptions.MaxImageResolution.svg', save_options=save_options)
        #ExEnd:MaxImageResolution

    #ExStart
    #ExFor:SvgSaveOptions
    #ExFor:SvgSaveOptions.export_embedded_images
    #ExFor:SvgSaveOptions.resource_saving_callback
    #ExFor:SvgSaveOptions.resources_folder
    #ExFor:SvgSaveOptions.resources_folder_alias
    #ExFor:SvgSaveOptions.save_format
    #ExSummary:Shows how to manipulate and print the URIs of linked resources created while converting a document to .svg.
    #def test_svg_resource_folder(self):

    #    doc = aw.Document(MY_DIR + "Rendering.docx")

    #    options = aw.saving.SvgSaveOptions()
    #    options.save_format = aw.saving.SaveFormat.SVG
    #    options.export_embedded_images = False
    #    options.resources_folder = ARTIFACTS_DIR + "SvgResourceFolder"
    #    options.resources_folder_alias = ARTIFACTS_DIR + "SvgResourceFolderAlias",
    #    options.show_page_border = False
    #    options.resource_saving_callback = ExSvgSaveOptions.ResourceUriPrinter()

    #    os.mkdir(options.resources_folder_alias)

    #    doc.save(ARTIFACTS_DIR + "SvgSaveOptions.SvgResourceFolder.svg", options)

    #class ResourceUriPrinter(aw.saving.IResourceSavingCallback):
    #    """Counts and prints URIs of resources contained by as they are converted to .svg."""

    #    def __init__(self):
    #        self.saved_resource_count = 0

    #    def resource_saving(self, args: aw.saving.ResourceSavingArgs):
    #        self.saved_resource_count += 1
    #        print(f"Resource #{self.saved_resource_count} \"{args.resource_file_name}\"")
    #        print("\t" + args.resource_file_uri)

    #ExEnd
