scrollbar_style = r'''
    .overflow-y-auto::-webkit-scrollbar {
        width: 10px;
    }
    .overflow-y-auto::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    .overflow-y-auto::-webkit-scrollbar-thumb {
        background: #888;
    }
    .overflow-y-auto::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
    .overflow-y-auto {
        padding-right: 10px;  # add right padding to the element
    }
    '''

with ui.row().classes('w-full max-w-2xl mx-auto h-[500px] overflow-y-auto px-2'):  # decrease horizontal padding
