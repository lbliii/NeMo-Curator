# Documentation Deployment to S3

This guide explains how to deploy the NeMo Curator documentation to the S3 hosting environment.

## Prerequisites

1. **AWS CLI**: Install and configure AWS CLI with appropriate credentials
   ```bash
   pip install awscli
   aws configure
   ```

2. **S3 Permissions**: Ensure your AWS credentials have the following permissions for the bucket `s3://brightspot-assets-prod/developer/docs/nemo/curator/`:
   - `s3:ListBucket`
   - `s3:GetObject`
   - `s3:PutObject`
   - `s3:DeleteObject`

3. **Documentation Environment**: Set up the docs environment
   ```bash
   make docs-env
   source .venv-docs/bin/activate
   ```

## Deployment Commands

### Quick Deployment

Build and deploy the latest GA documentation to S3:

```bash
make docs-deploy
```

This command:
1. Runs `make docs-publish-ga` to build the documentation
2. Auto-detects the version from `project.json`
3. Backs up the current `/latest/` to a versioned directory
4. Deploys the new build to `/latest/`
5. Updates version management files

### Dry Run

See what would be deployed without making changes:

```bash
make docs-deploy-dry-run
```

### Deploy Specific Version

Deploy with a specific version override:

```bash
make docs-deploy-version VERSION=1.2.3
```

### Direct Script Usage

You can also use the deployment script directly for more control:

```bash
# Basic deployment
./scripts/deploy-docs.sh

# Dry run
./scripts/deploy-docs.sh --dry-run

# Specific version
./scripts/deploy-docs.sh --version 1.2.3

# Skip backing up current latest
./scripts/deploy-docs.sh --no-backup

# Help
./scripts/deploy-docs.sh --help
```

## S3 Structure

The deployment creates the following structure in S3:

```
s3://brightspot-assets-prod/developer/docs/nemo/curator/
├── latest/                    # Current release (always points to newest)
│   ├── index.html
│   ├── versions1.json         # Version switcher config
│   └── ...                    # All documentation files
├── 25.7/                      # Previous version (backed up)
│   ├── index.html
│   └── ...
├── 25.6/                      # Older version
│   └── ...
└── versions1.json             # Root-level version config
```

## Version Management

The system uses `versions1.json` for version switching in the documentation:

- **`/latest/versions1.json`**: Controls the version switcher widget
- **`/versions1.json`**: Root-level version index

When deploying:
1. The current `/latest/` is backed up to `/{previous-version}/`
2. The new build is deployed to `/latest/`
3. `versions1.json` is updated to include all versions
4. The current version is marked as `preferred: true` and points to `../latest`
5. Previous versions point to their respective directories (`../25.7`, etc.)

## Access URLs

After deployment, documentation is available at:

- **Latest**: https://docs.nvidia.com/nemo/curator/latest/
- **Specific version**: https://docs.nvidia.com/nemo/curator/25.7/
- **Version switcher**: Available in the top navigation bar

## Troubleshooting

### AWS Permissions Issues

If you get permission errors:

1. Verify your AWS credentials:
   ```bash
   aws sts get-caller-identity
   ```

2. Test S3 access:
   ```bash
   aws s3 ls s3://brightspot-assets-prod/developer/docs/nemo/curator/
   ```

### Build Issues

If the deployment fails due to build issues:

1. Ensure the documentation builds successfully:
   ```bash
   make docs-clean
   make docs-publish-ga
   ```

2. Check for build warnings/errors in the output

### Version Detection Issues

If version auto-detection fails:

1. Check that `docs/_build/html/project.json` exists
2. Manually specify version: `./scripts/deploy-docs.sh --version X.Y.Z`

## Development Workflow

Recommended workflow for documentation updates:

1. **Make changes** to documentation files
2. **Test locally**: `make docs-live-ga`
3. **Build for production**: `make docs-publish-ga`
4. **Review build output** in `docs/_build/html/`
5. **Dry run deployment**: `make docs-deploy-dry-run`
6. **Deploy**: `make docs-deploy`

## Cache Control

The deployment script sets appropriate cache headers:

- **Documentation files**: `public, max-age=3600` (1 hour)
- **Version files**: `public, max-age=300` (5 minutes)

This ensures reasonable caching while allowing version updates to propagate quickly. 