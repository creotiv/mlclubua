Задачи на неделю:

Тероия:
* https://www.youtube.com/watch?v=vT1JzLTH4G4&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv - Лекцции 4-7
* https://distill.pub/2016/deconv-checkerboard/ - Проблемы деконволюшена(правильное название Transpose Convolution)
* https://distill.pub/2017/feature-visualization/ - Визуализация сетей

Практика:
* http://cs231n.github.io/assignments2017/assignment1/ - задачи Q4-5
* Используйте Features Vectors(как в Q5) для нахождения похожих картинок. Подсказка: многомерные вектора лучше всего сравнивать через cosine distance. Сравнить матрицу векторов с самой собой можно используя https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.spatial.distance.pdist.html Если захотите построить индекс для поиска, то самым простым и действенным вариантом будет использование Annoy Index https://github.com/spotify/annoy
* Используйте cosine distance для кластеризации картинок на 2мерной плоскости. Подсказка: чтобы сжать размерность вектора с N-мерного до 2-мерного воспользуйтесь https://github.com/danielfrg/tsne Пример кода для генерации картинки в файле **manifold.py**
