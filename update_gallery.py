import os
import re

# Configuration
portfolio_dir = 'images/portfolio'
html_file = 'works.html'
allowed_extensions = ('.jpg', '.jpeg', '.png', '.webp')

def update_gallery():
    # 1. Get list of images
    if not os.path.exists(portfolio_dir):
        print(f"Error: Folder {portfolio_dir} does not exist!")
        return

    images = [f for f in os.listdir(portfolio_dir) if f.lower().endswith(allowed_extensions)]
    images.sort()  # Alphabetical sorting
    
    print(f"Found {len(images)} images in {portfolio_dir}")
    
    # 2. Generate HTML blocks
    html_blocks = []
    for img in images:
        block = f'''                            <div class="col-md-4 col-lg-3 portfolio-item animate-box" data-animate-effect="fadeInUp">
                                <a href="images/portfolio/{img}" class="d-block miklas-photo-item" data-caption="Portfolio Image" data-fancybox="gallery">
                                    <img src="images/portfolio/{img}" alt="" class="img-fluid">
                                </a>
                            </div>'''
        html_blocks.append(block)

    all_photos_html = "\n".join(html_blocks)
    
    # 3. Update HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the Portfolio Grid section and its row container
    # Look for the specific pattern in works.html
    portfolio_grid_pattern = r'(<div class="portfolio-grid miklas-photos">\s*<div class="row">)(.*?)(</div>\s*</div>\s*</div>\s*</div>)'
    
    match = re.search(portfolio_grid_pattern, content, re.DOTALL)
    
    if match:
        # Replace the content between the row tags
        start_tag = match.group(1)
        end_tag = match.group(3)
        
        # Create new content with generated HTML blocks
        new_content = start_tag + "\n" + all_photos_html + "\n                        " + end_tag
        
        # Replace in the full content
        updated_content = content.replace(match.group(0), new_content)
        
        # Write back to file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ Successfully updated {html_file} with {len(images)} portfolio items!")
        print(f"Updated images: {', '.join(images)}")
        
    else:
        print("❌ Could not find the Portfolio Grid section in works.html")
        print("Looking for pattern: <div class=\"portfolio-grid miklas-photos\"> followed by <div class=\"row\">")
        return

if __name__ == "__main__":
    update_gallery()