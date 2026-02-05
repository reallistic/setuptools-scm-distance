from setuptools_scm.version import SEMVER_LEN, ScmVersion


def get_tag_distance(scm_version: ScmVersion) -> str:
    if scm_version.exact:
        return scm_version.format_with("tag")
    else:
        version_parts = list(scm_version.tag.release)
        if len(version_parts) != SEMVER_LEN or version_parts[-1] != 0:
            raise ValueError(f"tag {scm_version.tag.release!r} is not in format v#.#.0")
        version_parts[2] = scm_version.distance
        return ".".join([str(a) for a in version_parts])
