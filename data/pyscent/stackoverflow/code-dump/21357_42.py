class MoviesViewSet(viewsets.ModelViewSet):
    queryset            = Movie.objects.all()
    serializer_class    = MovieSerializer
    permission_classes  = [IsAuthenticated, ]

    def get_queryset(self):
        return self.queryset

    def get_object(self):
        movie_id = self.kwargs['pk']
        return self.get_queryset().filter(id=movie_id)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except (Movie.DoesNotExist, KeyError):
            return Response({"error": "Requested Movie does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset    = self.get_queryset()
        serializer  = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
