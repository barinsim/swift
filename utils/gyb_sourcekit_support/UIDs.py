class KEY(object):
    def __init__(self, internal_name, external_name):
        self.internalName = internal_name
        self.externalName = external_name


class REQUEST(object):
    def __init__(self, internal_name, external_name):
        self.internalName = internal_name
        self.externalName = external_name


class KIND(object):
    def __init__(self, internal_name, external_name):
        self.internalName = internal_name
        self.externalName = external_name


UID_KEYS = [
    KEY('VersionMajor', 'key.version_major'),
    KEY('VersionMinor', 'key.version_minor'),
    KEY('VersionPatch', 'key.version_patch'),
    KEY('Results', 'key.results'),
    KEY('Request', 'key.request'),
    KEY('Notification', 'key.notification'),
    KEY('Kind', 'key.kind'),
    KEY('AccessLevel', 'key.accessibility'),
    KEY('SetterAccessLevel', 'key.setter_accessibility'),
    KEY('Keyword', 'key.keyword'),
    KEY('Name', 'key.name'),
    KEY('USR', 'key.usr'),
    KEY('OriginalUSR', 'key.original_usr'),
    KEY('DefaultImplementationOf', 'key.default_implementation_of'),
    KEY('InterestedUSR', 'key.interested_usr'),
    KEY('GenericParams', 'key.generic_params'),
    KEY('GenericRequirements', 'key.generic_requirements'),
    KEY('DocFullAsXML', 'key.doc.full_as_xml'),
    KEY('Line', 'key.line'),
    KEY('Column', 'key.column'),
    KEY('ReceiverUSR', 'key.receiver_usr'),
    KEY('Receivers', 'key.receivers'),
    KEY('IsDynamic', 'key.is_dynamic'),
    KEY('IsImplicit', 'key.is_implicit'),
    KEY('FilePath', 'key.filepath'),
    KEY('ModuleInterfaceName', 'key.module_interface_name'),
    KEY('Hash', 'key.hash'),
    KEY('CompilerArgs', 'key.compilerargs'),
    KEY('Severity', 'key.severity'),
    KEY('Offset', 'key.offset'),
    KEY('Length', 'key.length'),
    KEY('SourceFile', 'key.sourcefile'),
    KEY('SourceText', 'key.sourcetext'),
    KEY('PrimaryFile', 'key.primary_file'),
    KEY('EnableSyntaxMap', 'key.enablesyntaxmap'),
    KEY('EnableStructure', 'key.enablesubstructure'),
    KEY('ID', 'key.id'),
    KEY('Description', 'key.description'),
    KEY('TypeName', 'key.typename'),
    KEY('RuntimeName', 'key.runtime_name'),
    KEY('SelectorName', 'key.selector_name'),
    KEY('AnnotatedDecl', 'key.annotated_decl'),
    KEY('FullyAnnotatedDecl', 'key.fully_annotated_decl'),
    KEY('FullyAnnotatedGenericSignature',
        'key.fully_annotated_generic_signature'),
    KEY('DocBrief', 'key.doc.brief'),
    KEY('Context', 'key.context'),
    KEY('TypeRelation', 'key.typerelation'),
    KEY('ModuleImportDepth', 'key.moduleimportdepth'),
    KEY('NumBytesToErase', 'key.num_bytes_to_erase'),
    KEY('NotRecommended', 'key.not_recommended'),
    KEY('Annotations', 'key.annotations'),
    KEY('DiagnosticStage', 'key.diagnostic_stage'),
    KEY('SyntaxMap', 'key.syntaxmap'),
    KEY('IsSystem', 'key.is_system'),
    KEY('Related', 'key.related'),
    KEY('Inherits', 'key.inherits'),
    KEY('Conforms', 'key.conforms'),
    KEY('Extends', 'key.extends'),
    KEY('Dependencies', 'key.dependencies'),
    KEY('Entities', 'key.entities'),
    KEY('NameOffset', 'key.nameoffset'),
    KEY('NameLength', 'key.namelength'),
    KEY('BodyOffset', 'key.bodyoffset'),
    KEY('BodyLength', 'key.bodylength'),
    KEY('DocOffset', 'key.docoffset'),
    KEY('DocLength', 'key.doclength'),
    KEY('IsActive', 'key.is_active'),
    KEY('IsLocal', 'key.is_local'),
    KEY('InheritedTypes', 'key.inheritedtypes'),
    KEY('Attributes', 'key.attributes'),
    KEY('Attribute', 'key.attribute'),
    KEY('Elements', 'key.elements'),
    KEY('SubStructure', 'key.substructure'),
    KEY('Ranges', 'key.ranges'),
    KEY('Fixits', 'key.fixits'),
    KEY('GeneratedBuffers', 'key.generated_buffers'),
    KEY('BufferText', 'key.buffer_text'),
    KEY('OriginalLocation', 'key.original_location'),
    KEY('Diagnostics', 'key.diagnostics'),
    KEY('EducationalNotePaths', 'key.educational_note_paths'),
    KEY('FormatOptions', 'key.editor.format.options'),
    KEY('CodeCompleteOptions', 'key.codecomplete.options'),
    KEY('TypeContextInfoOptions', 'key.typecontextinfo.options'),
    KEY('ConformingMethodListOptions', 'key.conformingmethods.options'),
    KEY('FilterRules', 'key.codecomplete.filterrules'),
    KEY('NextRequestStart', 'key.nextrequeststart'),
    KEY('Popular', 'key.popular'),
    KEY('Unpopular', 'key.unpopular'),
    KEY('Hide', 'key.hide'),
    KEY('Platform', 'key.platform'),
    KEY('IsDeprecated', 'key.is_deprecated'),
    KEY('IsUnavailable', 'key.is_unavailable'),
    KEY('IsOptional', 'key.is_optional'),
    KEY('IsAsync', 'key.is_async'),
    KEY('Message', 'key.message'),
    KEY('Introduced', 'key.introduced'),
    KEY('Deprecated', 'key.deprecated'),
    KEY('Obsoleted', 'key.obsoleted'),
    KEY('RemoveCache', 'key.removecache'),
    KEY('TypeUsr', 'key.typeusr'),
    KEY('ContainerTypeUsr', 'key.containertypeusr'),
    KEY('ModuleGroups', 'key.modulegroups'),
    KEY('BaseName', 'key.basename'),
    KEY('ArgNames', 'key.argnames'),
    KEY('SelectorPieces', 'key.selectorpieces'),
    KEY('NameKind', 'key.namekind'),
    KEY('LocalizationKey', 'key.localization_key'),
    KEY('IsZeroArgSelector', 'key.is_zero_arg_selector'),
    KEY('SwiftVersion', 'key.swift_version'),
    KEY('Value', 'key.value'),
    KEY('EnableDiagnostics', 'key.enablediagnostics'),
    KEY('GroupName', 'key.groupname'),
    KEY('ActionName', 'key.actionname'),
    KEY('SynthesizedExtension', 'key.synthesizedextensions'),
    KEY('UsingSwiftArgs', 'key.usingswiftargs'),
    KEY('Names', 'key.names'),
    KEY('UIDs', 'key.uids'),
    KEY('SyntacticOnly', 'key.syntactic_only'),
    KEY('ParentLoc', 'key.parent_loc'),
    KEY('IsTestCandidate', 'key.is_test_candidate'),
    KEY('Overrides', 'key.overrides'),
    KEY('AssociatedUSRs', 'key.associated_usrs'),
    KEY('ModuleName', 'key.modulename'),
    KEY('RelatedDecls', 'key.related_decls'),
    KEY('Simplified', 'key.simplified'),
    KEY('RangeContent', 'key.rangecontent'),
    KEY('CancelOnSubsequentRequest', 'key.cancel_on_subsequent_request'),
    KEY('RenameLocations', 'key.renamelocations'),
    KEY('Locations', 'key.locations'),
    KEY('NameType', 'key.nametype'),
    KEY('NewName', 'key.newname'),
    KEY('CategorizedEdits', 'key.categorizededits'),
    KEY('CategorizedRanges', 'key.categorizedranges'),
    KEY('RangesWorthNote', 'key.rangesworthnote'),
    KEY('Edits', 'key.edits'),
    KEY('EndLine', 'key.endline'),
    KEY('EndColumn', 'key.endcolumn'),
    KEY('ArgIndex', 'key.argindex'),
    KEY('Text', 'key.text'),
    KEY('Category', 'key.category'),
    KEY('Categories', 'key.categories'),
    KEY('IsFunctionLike', 'key.is_function_like'),
    KEY('IsNonProtocolType', 'key.is_non_protocol_type'),
    KEY('RefactorActions', 'key.refactor_actions'),
    KEY('RetrieveRefactorActions', 'key.retrieve_refactor_actions'),
    KEY('SymbolGraph', 'key.symbol_graph'),
    KEY('RetrieveSymbolGraph', 'key.retrieve_symbol_graph'),
    KEY('ParentContexts', 'key.parent_contexts'),
    KEY('ReferencedSymbols', 'key.referenced_symbols'),
    KEY('IsSPI', 'key.is_spi'),
    KEY('ActionUID', 'key.actionuid'),
    KEY('ActionUnavailableReason', 'key.actionunavailablereason'),
    KEY('CompileID', 'key.compileid'),
    KEY('CompilerArgsString', 'key.compilerargs-string'),
    KEY('ImplicitMembers', 'key.implicitmembers'),
    KEY('ExpectedTypes', 'key.expectedtypes'),
    KEY('AlternativeTypes', 'key.alternativetypes'),
    KEY('Members', 'key.members'),
    KEY('TypeBuffer', 'key.printedtypebuffer'),
    KEY('ExpressionTypeList', 'key.expression_type_list'),
    KEY('ExpressionOffset', 'key.expression_offset'),
    KEY('ExpressionLength', 'key.expression_length'),
    KEY('ExpressionType', 'key.expression_type'),
    KEY('VariableTypeList', 'key.variable_type_list'),
    KEY('VariableOffset', 'key.variable_offset'),
    KEY('VariableLength', 'key.variable_length'),
    KEY('VariableType', 'key.variable_type'),
    KEY('VariableTypeExplicit', 'key.variable_type_explicit'),
    KEY('FullyQualified', 'key.fully_qualified'),
    KEY('CanonicalizeType', 'key.canonicalize_type'),
    KEY('InternalDiagnostic', 'key.internal_diagnostic'),
    KEY('VFSName', 'key.vfs.name'),
    KEY('VFSOptions', 'key.vfs.options'),
    KEY('Files', 'key.files'),
    KEY('OptimizeForIDE', 'key.optimize_for_ide'),
    KEY('RequiredBystanders', 'key.required_bystanders'),
    KEY('ReusingASTContext', 'key.reusingastcontext'),
    KEY('CompletionMaxASTContextReuseCount',
        'key.completion_max_astcontext_reuse_count'),
    KEY('CompletionCheckDependencyInterval',
        'key.completion_check_dependency_interval'),
    KEY('AnnotatedTypename', 'key.annotated.typename'),
    KEY('CompileOperation', 'key.compile_operation'),
    KEY('EffectiveAccess', 'key.effective_access'),
    KEY('DeclarationLang', 'key.decl_lang'),
    KEY('SecondarySymbols', 'key.secondary_symbols'),
    # Before executing the actual request wait x ms. The request can be canceled
    # in this time. For cancellation testing purposes.
    KEY('SimulateLongRequest', 'key.simulate_long_request'),
    KEY('IsSynthesized', 'key.is_synthesized'),
    KEY('BufferName', 'key.buffer_name'),
    KEY('BarriersEnabled', 'key.barriers_enabled'),
    KEY('Expansions', 'key.expansions'),
    KEY('MacroRoles', 'key.macro_roles'),
    KEY('ExpandedMacroReplacements', 'key.expanded_macro_replacements'),
    KEY('IndexStorePath', 'key.index_store_path'),
    KEY('IndexUnitOutputPath', 'key.index_unit_output_path'),
]


UID_REQUESTS = [
    REQUEST('ProtocolVersion', 'source.request.protocol_version'),
    REQUEST('CompilerVersion', 'source.request.compiler_version'),
    REQUEST('CrashWithExit', 'source.request.crash_exit'),
    REQUEST('Demangle', 'source.request.demangle'),
    REQUEST('MangleSimpleClass', 'source.request.mangle_simple_class'),
    REQUEST('Index', 'source.request.indexsource'),
    REQUEST('DocInfo', 'source.request.docinfo'),
    REQUEST('CodeComplete', 'source.request.codecomplete'),
    REQUEST('CodeCompleteOpen', 'source.request.codecomplete.open'),
    REQUEST('CodeCompleteClose', 'source.request.codecomplete.close'),
    REQUEST('CodeCompleteUpdate', 'source.request.codecomplete.update'),
    REQUEST('CodeCompleteCacheOnDisk',
            'source.request.codecomplete.cache.ondisk'),
    REQUEST('CodeCompleteSetPopularAPI',
            'source.request.codecomplete.setpopularapi'),
    REQUEST('CodeCompleteSetCustom', 'source.request.codecomplete.setcustom'),
    REQUEST('TypeContextInfo', 'source.request.typecontextinfo'),
    REQUEST('ConformingMethodList', 'source.request.conformingmethods'),
    REQUEST('ActiveRegions', 'source.request.activeregions'),
    REQUEST('CursorInfo', 'source.request.cursorinfo'),
    REQUEST('RangeInfo', 'source.request.rangeinfo'),
    REQUEST('RelatedIdents', 'source.request.relatedidents'),
    REQUEST('EditorOpen', 'source.request.editor.open'),
    REQUEST('EditorOpenInterface', 'source.request.editor.open.interface'),
    REQUEST('EditorOpenHeaderInterface',
            'source.request.editor.open.interface.header'),
    REQUEST('EditorOpenSwiftSourceInterface',
            'source.request.editor.open.interface.swiftsource'),
    REQUEST('EditorOpenSwiftTypeInterface',
            'source.request.editor.open.interface.swifttype'),
    REQUEST('EditorExtractTextFromComment',
            'source.request.editor.extract.comment'),
    REQUEST('EditorClose', 'source.request.editor.close'),
    REQUEST('EditorReplaceText', 'source.request.editor.replacetext'),
    REQUEST('EditorFormatText', 'source.request.editor.formattext'),
    REQUEST('EditorExpandPlaceholder',
            'source.request.editor.expand_placeholder'),
    REQUEST('EditorFindUSR', 'source.request.editor.find_usr'),
    REQUEST('EditorFindInterfaceDoc',
            'source.request.editor.find_interface_doc'),
    REQUEST('BuildSettingsRegister', 'source.request.buildsettings.register'),
    REQUEST('ModuleGroups', 'source.request.module.groups'),
    REQUEST('NameTranslation', 'source.request.name.translation'),
    REQUEST('MarkupToXML', 'source.request.convert.markup.xml'),
    REQUEST('Statistics', 'source.request.statistics'),
    REQUEST('SyntacticRename', 'source.request.syntacticrename'),
    REQUEST('FindRenameRanges', 'source.request.find-syntactic-rename-ranges'),
    REQUEST('FindLocalRenameRanges',
            'source.request.find-local-rename-ranges'),
    REQUEST('SemanticRefactoring', 'source.request.semantic.refactoring'),
    REQUEST('EnableCompileNotifications',
            'source.request.enable-compile-notifications'),
    REQUEST('TestNotification', 'source.request.test_notification'),
    REQUEST('CollectExpressionType', 'source.request.expression.type'),
    REQUEST('CollectVariableType', 'source.request.variable.type'),
    REQUEST('GlobalConfiguration', 'source.request.configuration.global'),
    REQUEST('DependencyUpdated', 'source.request.dependency_updated'),
    REQUEST('Diagnostics', 'source.request.diagnostics'),
    REQUEST('Compile', 'source.request.compile'),
    REQUEST('CompileClose', 'source.request.compile.close'),
    REQUEST('EnableRequestBarriers', 'source.request.enable_request_barriers'),
    REQUEST('SyntacticMacroExpansion',
            'source.request.syntactic_macro_expansion'),
    REQUEST('IndexToStore', 'source.request.index_to_store'),
]


UID_KINDS = [
    KIND('DeclFunctionFree', 'source.lang.swift.decl.function.free'),
    KIND('RefFunctionFree', 'source.lang.swift.ref.function.free'),
    KIND('DeclMethodInstance',
         'source.lang.swift.decl.function.method.instance'),
    KIND('RefMethodInstance',
         'source.lang.swift.ref.function.method.instance'),
    KIND('DeclMethodStatic', 'source.lang.swift.decl.function.method.static'),
    KIND('RefMethodStatic', 'source.lang.swift.ref.function.method.static'),
    KIND('DeclMethodClass', 'source.lang.swift.decl.function.method.class'),
    KIND('RefMethodClass', 'source.lang.swift.ref.function.method.class'),
    KIND('DeclAccessorGetter',
         'source.lang.swift.decl.function.accessor.getter'),
    KIND('RefAccessorGetter',
         'source.lang.swift.ref.function.accessor.getter'),
    KIND('DeclAccessorSetter',
         'source.lang.swift.decl.function.accessor.setter'),
    KIND('RefAccessorSetter',
         'source.lang.swift.ref.function.accessor.setter'),
    KIND('DeclAccessorWillSet',
         'source.lang.swift.decl.function.accessor.willset'),
    KIND('RefAccessorWillSet',
         'source.lang.swift.ref.function.accessor.willset'),
    KIND('DeclAccessorDidSet',
         'source.lang.swift.decl.function.accessor.didset'),
    KIND('RefAccessorDidSet',
         'source.lang.swift.ref.function.accessor.didset'),
    KIND('DeclAccessorAddress',
         'source.lang.swift.decl.function.accessor.address'),
    KIND('RefAccessorAddress',
         'source.lang.swift.ref.function.accessor.address'),
    KIND('DeclAccessorMutableAddress',
         'source.lang.swift.decl.function.accessor.mutableaddress'),
    KIND('RefAccessorMutableAddress',
         'source.lang.swift.ref.function.accessor.mutableaddress'),
    KIND('DeclAccessorRead',
         'source.lang.swift.decl.function.accessor.read'),
    KIND('RefAccessorRead',
         'source.lang.swift.ref.function.accessor.read'),
    KIND('DeclAccessorModify',
         'source.lang.swift.decl.function.accessor.modify'),
    KIND('RefAccessorModify',
         'source.lang.swift.ref.function.accessor.modify'),
    KIND('DeclAccessorInit',
         'source.lang.swift.decl.function.accessor.init'),
    KIND('RefAccessorInit',
         'source.lang.swift.ref.function.accessor.init'),
    KIND('DeclConstructor', 'source.lang.swift.decl.function.constructor'),
    KIND('RefConstructor', 'source.lang.swift.ref.function.constructor'),
    KIND('DeclDestructor', 'source.lang.swift.decl.function.destructor'),
    KIND('RefDestructor', 'source.lang.swift.ref.function.destructor'),
    KIND('DeclFunctionPrefixOperator',
         'source.lang.swift.decl.function.operator.prefix'),
    KIND('DeclFunctionPostfixOperator',
         'source.lang.swift.decl.function.operator.postfix'),
    KIND('DeclFunctionInfixOperator',
         'source.lang.swift.decl.function.operator.infix'),
    KIND('RefFunctionPrefixOperator',
         'source.lang.swift.ref.function.operator.prefix'),
    KIND('RefFunctionPostfixOperator',
         'source.lang.swift.ref.function.operator.postfix'),
    KIND('RefFunctionInfixOperator',
         'source.lang.swift.ref.function.operator.infix'),
    KIND('DeclPrecedenceGroup', 'source.lang.swift.decl.precedencegroup'),
    KIND('RefPrecedenceGroup', 'source.lang.swift.ref.precedencegroup'),
    KIND('DeclSubscript', 'source.lang.swift.decl.function.subscript'),
    KIND('RefSubscript', 'source.lang.swift.ref.function.subscript'),
    KIND('DeclVarGlobal', 'source.lang.swift.decl.var.global'),
    KIND('RefVarGlobal', 'source.lang.swift.ref.var.global'),
    KIND('DeclVarInstance', 'source.lang.swift.decl.var.instance'),
    KIND('RefVarInstance', 'source.lang.swift.ref.var.instance'),
    KIND('DeclVarStatic', 'source.lang.swift.decl.var.static'),
    KIND('RefVarStatic', 'source.lang.swift.ref.var.static'),
    KIND('DeclVarClass', 'source.lang.swift.decl.var.class'),
    KIND('RefVarClass', 'source.lang.swift.ref.var.class'),
    KIND('DeclVarLocal', 'source.lang.swift.decl.var.local'),
    KIND('RefVarLocal', 'source.lang.swift.ref.var.local'),
    KIND('DeclVarParam', 'source.lang.swift.decl.var.parameter'),
    KIND('DeclModule', 'source.lang.swift.decl.module'),
    KIND('DeclClass', 'source.lang.swift.decl.class'),
    KIND('RefClass', 'source.lang.swift.ref.class'),
    KIND('DeclActor', 'source.lang.swift.decl.actor'),
    KIND('RefActor', 'source.lang.swift.ref.actor'),
    KIND('DeclStruct', 'source.lang.swift.decl.struct'),
    KIND('RefStruct', 'source.lang.swift.ref.struct'),
    KIND('DeclEnum', 'source.lang.swift.decl.enum'),
    KIND('RefEnum', 'source.lang.swift.ref.enum'),
    KIND('DeclEnumCase', 'source.lang.swift.decl.enumcase'),
    KIND('DeclEnumElement', 'source.lang.swift.decl.enumelement'),
    KIND('RefEnumElement', 'source.lang.swift.ref.enumelement'),
    KIND('DeclProtocol', 'source.lang.swift.decl.protocol'),
    KIND('RefProtocol', 'source.lang.swift.ref.protocol'),
    KIND('DeclExtension', 'source.lang.swift.decl.extension'),
    KIND('DeclExtensionStruct', 'source.lang.swift.decl.extension.struct'),
    KIND('DeclExtensionClass', 'source.lang.swift.decl.extension.class'),
    KIND('DeclExtensionEnum', 'source.lang.swift.decl.extension.enum'),
    KIND('DeclExtensionProtocol', 'source.lang.swift.decl.extension.protocol'),
    KIND('DeclAssociatedType', 'source.lang.swift.decl.associatedtype'),
    KIND('RefAssociatedType', 'source.lang.swift.ref.associatedtype'),
    KIND('DeclOpaqueType', 'source.lang.swift.decl.opaquetype'),
    KIND('RefOpaqueType', 'source.lang.swift.ref.opaquetype'),
    KIND('DeclTypeAlias', 'source.lang.swift.decl.typealias'),
    KIND('RefTypeAlias', 'source.lang.swift.ref.typealias'),
    KIND('DeclGenericTypeParam', 'source.lang.swift.decl.generic_type_param'),
    KIND('RefGenericTypeParam', 'source.lang.swift.ref.generic_type_param'),
    KIND('DeclMacro', 'source.lang.swift.decl.macro'),
    KIND('RefMacro', 'source.lang.swift.ref.macro'),
    KIND('RefModule', 'source.lang.swift.ref.module'),
    KIND('CommentTag', 'source.lang.swift.commenttag'),
    KIND('StmtForEach', 'source.lang.swift.stmt.foreach'),
    KIND('StmtFor', 'source.lang.swift.stmt.for'),
    KIND('StmtWhile', 'source.lang.swift.stmt.while'),
    KIND('StmtRepeatWhile', 'source.lang.swift.stmt.repeatwhile'),
    KIND('StmtIf', 'source.lang.swift.stmt.if'),
    KIND('StmtGuard', 'source.lang.swift.stmt.guard'),
    KIND('StmtSwitch', 'source.lang.swift.stmt.switch'),
    KIND('StmtCase', 'source.lang.swift.stmt.case'),
    KIND('StmtBrace', 'source.lang.swift.stmt.brace'),
    KIND('ExprCall', 'source.lang.swift.expr.call'),
    KIND('ExprArg', 'source.lang.swift.expr.argument'),
    KIND('ExprArray', 'source.lang.swift.expr.array'),
    KIND('ExprDictionary', 'source.lang.swift.expr.dictionary'),
    KIND('ExprObjectLiteral', 'source.lang.swift.expr.object_literal'),
    KIND('ExprTuple', 'source.lang.swift.expr.tuple'),
    KIND('ExprClosure', 'source.lang.swift.expr.closure'),
    KIND('StructureElemId', 'source.lang.swift.structure.elem.id'),
    KIND('StructureElemExpr', 'source.lang.swift.structure.elem.expr'),
    KIND('StructureElemInitExpr',
         'source.lang.swift.structure.elem.init_expr'),
    KIND('StructureElemCondExpr',
         'source.lang.swift.structure.elem.condition_expr'),
    KIND('StructureElemPattern', 'source.lang.swift.structure.elem.pattern'),
    KIND('StructureElemTypeRef', 'source.lang.swift.structure.elem.typeref'),
    KIND('RangeSingleStatement', 'source.lang.swift.range.singlestatement'),
    KIND('RangeSingleExpression', 'source.lang.swift.range.singleexpression'),
    KIND('RangeSingleDeclaration',
         'source.lang.swift.range.singledeclaration'),
    KIND('RangeMultiStatement', 'source.lang.swift.range.multistatement'),
    KIND('RangeMultiTypeMemberDeclaration',
         'source.lang.swift.range.multitypememberdeclaration'),
    KIND('RangeInvalid', 'source.lang.swift.range.invalid'),
    KIND('NameObjc', 'source.lang.name.kind.objc'),
    KIND('NameSwift', 'source.lang.name.kind.swift'),
    KIND('Keyword', 'source.lang.swift.syntaxtype.keyword'),
    KIND('Identifier', 'source.lang.swift.syntaxtype.identifier'),
    KIND('Operator', 'source.lang.swift.syntaxtype.operator'),
    KIND('TypeIdentifier', 'source.lang.swift.syntaxtype.typeidentifier'),
    KIND('BuildConfigKeyword',
         'source.lang.swift.syntaxtype.buildconfig.keyword'),
    KIND('BuildConfigId', 'source.lang.swift.syntaxtype.buildconfig.id'),
    KIND('PoundDirectiveKeyword',
         'source.lang.swift.syntaxtype.pounddirective.keyword'),
    KIND('AttributeId', 'source.lang.swift.syntaxtype.attribute.id'),
    KIND('AttributeBuiltin', 'source.lang.swift.syntaxtype.attribute.builtin'),
    KIND('Number', 'source.lang.swift.syntaxtype.number'),
    KIND('String', 'source.lang.swift.syntaxtype.string'),
    KIND('StringInterpolation',
         'source.lang.swift.syntaxtype.string_interpolation_anchor'),
    KIND('Comment', 'source.lang.swift.syntaxtype.comment'),
    KIND('DocComment', 'source.lang.swift.syntaxtype.doccomment'),
    KIND('DocCommentField', 'source.lang.swift.syntaxtype.doccomment.field'),
    KIND('CommentMarker', 'source.lang.swift.syntaxtype.comment.mark'),
    KIND('CommentURL', 'source.lang.swift.syntaxtype.comment.url'),
    KIND('Placeholder', 'source.lang.swift.syntaxtype.placeholder'),
    KIND('ObjectLiteral', 'source.lang.swift.syntaxtype.objectliteral'),
    KIND('Expr', 'source.lang.swift.expr'),
    KIND('Stmt', 'source.lang.swift.stmt'),
    KIND('Type', 'source.lang.swift.type'),
    KIND('ForEachSequence', 'source.lang.swift.foreach.sequence'),
    KIND('DiagNote', 'source.diagnostic.severity.note'),
    KIND('DiagWarning', 'source.diagnostic.severity.warning'),
    KIND('DiagError', 'source.diagnostic.severity.error'),
    KIND('DiagDeprecation', 'source.diagnostic.category.deprecation'),
    KIND('DiagNoUsage', 'source.diagnostic.category.no_usage'),
    KIND('CodeCompletionEverything', 'source.codecompletion.everything'),
    KIND('CodeCompletionModule', 'source.codecompletion.module'),
    KIND('CodeCompletionKeyword', 'source.codecompletion.keyword'),
    KIND('CodeCompletionLiteral', 'source.codecompletion.literal'),
    KIND('CodeCompletionCustom', 'source.codecompletion.custom'),
    KIND('CodeCompletionIdentifier', 'source.codecompletion.identifier'),
    KIND('CodeCompletionDescription', 'source.codecompletion.description'),
    KIND('EditActive', 'source.edit.kind.active'),
    KIND('EditInactive', 'source.edit.kind.inactive'),
    KIND('EditSelector', 'source.edit.kind.selector'),
    KIND('EditString', 'source.edit.kind.string'),
    KIND('EditComment', 'source.edit.kind.comment'),
    KIND('EditMismatch', 'source.edit.kind.mismatch'),
    KIND('EditUnknown', 'source.edit.kind.unknown'),
    KIND('RenameRangeBase', 'source.refactoring.range.kind.basename'),
    KIND('RenameRangeKeywordBase',
         'source.refactoring.range.kind.keyword-basename'),
    KIND('RenameRangeParam',
         'source.refactoring.range.kind.parameter-and-whitespace'),
    KIND('RenameRangeNoncollapsibleParam',
         'source.refactoring.range.kind.noncollapsible-parameter'),
    KIND('RenameRangeDeclArgLabel',
         'source.refactoring.range.kind.decl-argument-label'),
    KIND('RenameRangeCallArgLabel',
         'source.refactoring.range.kind.call-argument-label'),
    KIND('RenameRangeCallArgColon',
         'source.refactoring.range.kind.call-argument-colon'),
    KIND('RenameRangeCallArgCombined',
         'source.refactoring.range.kind.call-argument-combined'),
    KIND('RenameRangeSelectorArgLabel',
         'source.refactoring.range.kind.selector-argument-label'),
    KIND('Definition', 'source.syntacticrename.definition'),
    KIND('Reference', 'source.syntacticrename.reference'),
    KIND('Call', 'source.syntacticrename.call'),
    KIND('Unknown', 'source.syntacticrename.unknown'),
    KIND('StatNumRequests', 'source.statistic.num-requests'),
    KIND('StatNumSemaRequests', 'source.statistic.num-semantic-requests'),
    KIND('StatInstructionCount', 'source.statistic.instruction-count'),
    KIND('Swift', 'source.lang.swift'),
    KIND('ObjC', 'source.lang.objc'),
    KIND('MacroRoleExpression', 'source.lang.swift.macro_role.expression'),
    KIND('MacroRoleDeclaration', 'source.lang.swift.macro_role.declaration'),
    KIND('MacroRoleCodeItem', 'source.lang.swift.macro_role.codeitem'),
    KIND('MacroRoleAccessor', 'source.lang.swift.macro_role.accessor'),
    KIND('MacroRoleMemberAttribute', 'source.lang.swift.macro_role.member_attribute'),
    KIND('MacroRoleMember', 'source.lang.swift.macro_role.member'),
    KIND('MacroRolePeer', 'source.lang.swift.macro_role.peer'),
    KIND('MacroRoleConformance', 'source.lang.swift.macro_role.conformance'),
    KIND('MacroRoleExtension', 'source.lang.swift.macro_role.extension'),
]
