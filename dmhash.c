/* 
 * Originally based on hashfn.c in the glusterfs project
 * Davies-Meyer hashing function implementation
*/

#include <python2.7/Python.h>
#include <stdint.h>
#include <stdlib.h>

#define DM_DELTA 0x9E3779B9
#define DM_FULLROUNDS 10 /* 32 is overkill, 16 is strong crypto */
#define DM_PARTROUNDS 6 /* 6 gets complete mixing */

static int
dm_round (int rounds, uint32_t *array, uint32_t *h0, uint32_t *h1)
{
        uint32_t sum = 0;
        int n = 0;
        uint32_t b0 = 0;
        uint32_t b1 = 0;

        b0 = *h0;
        b1 = *h1;

        n = rounds;

        do {
                sum += DM_DELTA;
                b0 += ((b1 << 4) + array[0])
                        ^ (b1 + sum)
                        ^ ((b1 >> 5) + array[1]);
                b1 += ((b0 << 4) + array[2])
                        ^ (b0 + sum)
                        ^ ((b0 >> 5) + array[3]);
        } while (--n);

        *h0 += b0;
        *h1 += b1;

        return 0;
}


static uint32_t
__pad (int len)
{
        uint32_t pad = 0;

        pad = (uint32_t) len | ((uint32_t) len << 8);
        pad |= pad << 16;

        return pad;
}

static PyObject *
method_dmhash (PyObject *self, PyObject *args)
{
        char *msg;
        int len;

        uint32_t h0 = 0x9464a485;
        uint32_t h1 = 0x542e1a94;
        uint32_t array[4];
        uint32_t pad = 0;
        int i = 0;
        int j = 0;
        int full_quads = 0;
        int full_words = 0;
        int full_bytes = 0;
        uint32_t *intmsg = NULL;
        int word = 0;

        if (!PyArg_ParseTuple(args, "si", &msg, &len))
                return NULL;

        intmsg = (uint32_t *) msg;
        pad = __pad (len);

        full_bytes = len;
        full_words = len / 4;
        full_quads = len / 16;

        for (i = 0; i < full_quads; i++) {
                for (j = 0; j < 4; j++) {
                        word = *intmsg;
                        array[j] = word;
                        intmsg++;
                        full_words--;
                        full_bytes -= 4;
                }
                dm_round (DM_PARTROUNDS, &array[0], &h0, &h1);
        }

        for (j = 0; j < 4; j++) {
                if (full_words) {
                        word = *intmsg;
                        array[j] = word;
                        intmsg++;
                        full_words--;
                        full_bytes -= 4;
                } else {
                        array[j] = pad;
                        while (full_bytes) {
                                array[j] <<= 8;
                                array[j] |= msg[len - full_bytes];
                                full_bytes--;
                        }
                }
        }
        dm_round (DM_FULLROUNDS, &array[0], &h0, &h1);

        return Py_BuildValue ("i", h0 ^ h1);
}

static PyMethodDef DmHashMethods[] = {
        {"dmhash",  method_dmhash, METH_VARARGS, "DM Hash."},
        {NULL, NULL, 0, NULL} /* Sentinel */
};

PyMODINIT_FUNC
initdmhash (void)
{
    (void) Py_InitModule("dmhash", DmHashMethods);
}
