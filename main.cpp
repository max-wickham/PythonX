
#include <boost/python.hpp>
namespace py = boost::python;
#include <iostream>
using namespace std;
using namespace boost::python;
#include <string>
// g++ main.cpp `pkg-config python3-embed --cflags --libs` -lboost_python310
// export CPLUS_INCLUDE_PATH="$CPLUS_INCLUDE_PATH:/usr/include/python3.10/"
class Test
{
public :
    int x = 5;
    Test()
    {
    }
    void print(){
        cout << this->x;
    }

    PyObject *get(){
        return nullptr;
    }
};

struct Test_to_python_str
{
    static PyObject* convert(Test const& s)
    {
        return boost::python::incref(
              boost::python::object(
                s.x).ptr());
    }
};

// BOOST_PYTHON_MODULE(Test)
// {
//     def("greet", greet);
// }

int main()
{
    Py_Initialize(); // Must be called first
    boost::python::to_python_converter<
    Test,
    Test_to_python_str>();
    try
    {
        py::object global = py::import("__main__").attr("__dict__");
        // ['hoge','fuga','piyo']Create a list called
        py::object number = py::eval("5", global);
        py::object print = py::eval("print", global);
        // 「','.join(list), And combine the strings in the list separated by commas.
        Test *x = new Test();
        // py::object result = print.attr("__call__")(x);
        boost::python::call<void>(print.ptr(),x);

        // Convert the result to string type and output
        //  std::string resultStr = py::extract<std::string>(result);
        //  std::cout << resultStr << std::endl;
    }
    catch (const py::error_already_set &)
    {
        // If an error occurs while executing Python code, the error content is displayed.
        PyErr_Print();
    }


    return 0;
}