import 'package:dart/dart.dart' as dart;

void main(List<String> arguments) {
    List<String> grid = [" /","/ "];
    int res = dart.Solution().regionsBySlashes(grid);
    print(res);
}
