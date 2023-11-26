import argparse

def main():
    parser = argparse.ArgumentParser(description='2D Image Selector')
    parser.add_argument('image', help='Image file path')
    parser.add_argument('--title', help='Window title', default='2D Image Selector')
    args = parser.parse_args()

    print(f'Image "{args.image}"')

    app = Select2DApp(args.title)  # Pass the title as an optional argument
    app.load_image(args.image)
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
