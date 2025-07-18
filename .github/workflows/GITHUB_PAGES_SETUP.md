# GitHub Pages Setup Guide

This guide explains how to set up GitHub Pages for your NeMo Curator documentation.

## Initial Setup

### 1. Enable GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select **GitHub Actions**
4. Save the settings

### 2. Branch Protection (Recommended)

For production deployments, consider setting up branch protection for your main branch:

1. Go to **Settings** → **Branches**
2. Add a branch protection rule for `main`
3. Enable "Require status checks to pass before merging"
4. Select the documentation build check

## Workflow Features

### Automatic Builds

The workflow will automatically build and deploy documentation when:

- Code is pushed to the `main` branch
- Documentation files are changed in the `docs/` directory
- The `Makefile` or `requirements-docs.txt` are updated

### Build Environments

The workflow supports different build environments:

- **GA (General Availability)**: Default for main branch deployments
- **EA (Early Access)**: Includes all content including early access features  
- **Internal**: Internal documentation build
- **Draft**: Development builds with all content
- **Default**: Standard build without special tags

### Manual Deployments

You can manually trigger builds with different environments:

1. Go to **Actions** → **Build and Deploy Documentation**
2. Click **Run workflow**
3. Select your desired build environment
4. Click **Run workflow**

### Pull Request Previews

For pull requests, the workflow will:

- Build documentation with the `draft` environment
- Upload the built docs as an artifact
- Comment on the PR with download instructions
- Artifacts are retained for 7 days

## Build Variants

Based on your Makefile, the following build commands are used:

- **Production builds** (main branch): `make docs-publish` (fails on warnings)
- **Development builds** (PRs/branches): `make docs-html` (warnings allowed)

## Environment Variables

The workflow uses the `DOCS_ENV` variable to control build variants:

```bash
# Build for General Availability (excludes EA-only content)
make docs-html DOCS_ENV=ga

# Build for Early Access (includes all content)
make docs-html DOCS_ENV=ea

# Build for development (draft mode)
make docs-html DOCS_ENV=draft
```

## Conditional Content

Your documentation supports conditional content based on build tags. Content can be:

- **File-level exclusion**: Using frontmatter `only: not ga`
- **Grid card conditional rendering**: Using `:only:` directive
- **Toctree conditional rendering**: Hiding sections based on build environment

## Troubleshooting

### Build Failures

If builds fail:

1. Check the Actions logs for detailed error messages
2. Ensure all dependencies in `requirements-docs.txt` are valid
3. Test builds locally using `make docs-env && make docs-html`
4. For production builds, fix any Sphinx warnings (they cause failures)

### Permission Issues

If deployment fails with permission errors:

1. Ensure GitHub Pages is configured to use **GitHub Actions** as source
2. Check that the repository has Pages enabled
3. Verify the workflow has the correct permissions (already configured)

### Missing Dependencies

If you need additional Python packages:

1. Add them to `requirements-docs.txt`
2. Commit and push the changes
3. The workflow will automatically use the updated requirements

## Local Development

To build documentation locally:

```bash
# Set up environment
make docs-env

# Activate environment
source .venv-docs/bin/activate

# Build documentation
make docs-html

# Start live-reload server
make docs-live
```

## Customization

### Changing Build Environment

To change the default build environment for main branch:

1. Edit `.github/workflows/docs.yml`
2. Modify the `DOCS_ENV="ga"` line in the build step
3. Commit and push changes

### Adding Build Steps

To add additional build steps:

1. Edit the workflow file `.github/workflows/docs.yml`
2. Add steps before or after the build step
3. Test with a pull request first

### Custom Domains

To use a custom domain:

1. Add a `CNAME` file to your repository root
2. Configure your domain's DNS to point to GitHub Pages
3. Update the Pages settings in your repository

## Monitoring

### Build Status

Monitor build status:

- **Actions tab**: See all workflow runs
- **Repository badges**: Add status badges to your README
- **Email notifications**: Configure in your GitHub notification settings

### Performance

The workflow includes several optimizations:

- **Dependency caching**: Speeds up subsequent builds
- **Path filtering**: Only builds when relevant files change
- **Concurrent deployment protection**: Prevents conflicts

## Security Considerations

The workflow:

- Uses specific action versions (pinned for security)
- Has minimal permissions (only what's needed for Pages)
- Doesn't expose sensitive information in logs
- Uses GitHub's secure artifact storage

## Support

For issues with:

- **Workflow problems**: Check the Actions logs and this guide
- **Documentation content**: Test builds locally first
- **GitHub Pages**: Consult GitHub's Pages documentation
- **Sphinx issues**: Check Sphinx documentation and your `conf.py` 