# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import jpype
from multiprocessing import Process, Queue, cpu_count
from Queue import Full
from Queue import Empty
from .MetaMap import MetaMap
from .Concept import Corpus

class JPypeBackend(MetaMap):
    def __init__(self):
        jpype.startJVM(jpype.getDefaultJVMPath()(),
                       '-ea',
                       'Djava.class.path=' + 'TMP',
                       *(extra_jvm_args or []))
