#include <Python.h>

int main(int argc, char *argv[])
{
    PyObject *pName, *pModule, *pDict, *pFunc, *pValue, *pArgs;
/*
    if (argc < 3) 
    {
        printf("Usage: exe_name python_source function_name\n");
        return 1;
    }
*/
    // Initialize the Python Interpreter
    Py_Initialize();

    // Build the name object
    pName = PyUnicode_FromString(argv[1]);

    // Load the module object
    pModule = PyImport_Import(pName);

    // pDict is a borrowed reference 
    pDict = PyModule_GetDict(pModule);

  //  pFunc = PyDict_GetItemString(pDict, "initfile", argv[2]);

  //  pFunc = PyDict_GetItemString(pDict, "write");

  //  pFunc = PyDict_GetItemString(pDict, "writex");
    // pFunc is also a borrowed reference 
    pFunc = PyDict_GetItemString(pDict, argv[2]);

    if (PyCallable_Check(pFunc)) 
    {
        if( argc > 3 )
        {
            pArgs = PyTuple_New(argc - 3);
            for (int i = 0; i < argc - 3; i++)
            {
                pValue = PyInt_FromLong(atoi(argv[i + 3]));
                if (!pValue)
                {
                    PyErr_Print();
                    return 1;
                }
                PyTuple_SetItem(pArgs, i, pValue);    
            }
            
        pValue = PyObject_CallObject(pFunc, pArgs);

        if (pArgs != NULL)
        {
            Py_DECREF(pArgs);
        }
        } else
        {
            pValue = PyObject_CallObject(pFunc, NULL);
        }

        if (pValue != NULL) 
        {
            printf("Return of call : %d\n", PyInt_AsLong(pValue));
            Py_DECREF(pValue);
        }
        else 
        {
            PyErr_Print();
        }
    } else 
    {
        PyErr_Print();
    }

    // Clean up
    //Py_DECREF(pModule);
    //Py_DECREF(pName);

    // Finish the Python Interpreter
    Py_Finalize();

    return 0;
}
