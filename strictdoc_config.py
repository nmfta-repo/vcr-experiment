from strictdoc.core.project_config import ProjectConfig, ProjectFeature


def create_config() -> ProjectConfig:
    return ProjectConfig(
        project_title="Heavy Duty Vehicle Cybersecurity Requirements (HD VCR)",
        include_doc_paths=[
            "*.sdoc",
        ],
        project_features=[
            ProjectFeature.TABLE_SCREEN,
            ProjectFeature.TRACEABILITY_SCREEN,
            ProjectFeature.DEEP_TRACEABILITY_SCREEN,
            ProjectFeature.SEARCH,
        ],
    )
