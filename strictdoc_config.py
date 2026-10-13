from strictdoc.core.project_config import ProjectConfig


def create_config() -> ProjectConfig:
    return ProjectConfig(
        project_title="Heavy Duty Vehicle Cybersecurity Requirements (HD VCR)",
        include_doc_paths=[
            "*.sdoc",
        ],
        project_features=[],
    )
